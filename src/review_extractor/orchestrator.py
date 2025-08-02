
import boto3
import os
import logging
from twelvelabs import TwelveLabs
from twelvelabs.models.task import Task
from .mongo_client import AtlasClient
from datetime import datetime, timezone
from moviepy import VideoFileClip
from google import genai
from dotenv import load_dotenv

load_dotenv()
# The client gets the API key from the environment variable `GEMINI_API_KEY`.

logger = logging.getLogger(__name__)


class Orchestrator:

    def __init__(self, api_key: str, atlas_client: AtlasClient):
        self.client = TwelveLabs(api_key=api_key)
        self.atlas_client = atlas_client
        self.s3 = boto3.client('s3')

    def start(self, record: dict) -> dict:
        bucket = record['s3']['bucket']['name']
        s3_key = record['s3']['object']['key']
        logger.info(f"Processing file from bucket: {bucket}, key: {s3_key}")
        client = genai.Client()
        
        # 1. Download the file from S3
        file, file_path = self.get_file(bucket, s3_key)
        duration = self.get_video_duration_moviepy(file_path)
        
        # 2. Retrived current video metadata from MongoDB
        video_metadata = self.atlas_client.find_video_metadata(s3_key)
        logger.info(f"Video metadata: {video_metadata}")
        # 3. Check if video index already exists in MongoDB
        myfile = client.files.upload(file=file_path)
        account_details = self.atlas_client.find_account_details(video_metadata['discord_id'])
        prompts = account_details.get("prompts", [])
        self.atlas_client.update_video_metadata(s3_key,
                                                {
                                                 "video_id": myfile.name,
                                                 "status":"INDEXING",
                                                 "prompts":prompts,
                                                 "duration": f"{duration} seconds",
                                                 "updated_at": datetime.now(timezone.utc)}
                                                )

        os.remove(file_path)     
        return {"video_id": myfile.name, "key_s3": s3_key}

    def get_file(self, bucket, key):
        file_name = key.split('/')[-1]
        local_path = f'/tmp/{file_name}'
        self.s3.download_file(bucket, key, local_path)
        logger.info(f"Downloaded {key} to {local_path}")

        # 3. Process the file (your logic here)
        # Example: Just print size, but here you could use ffmpeg, analyze, etc.
        return open(local_path, 'rb'), local_path
            # return {'file': (file_name, f)}
        
    def on_task_update(self, task: Task):
        print(f"  Status={task.status}")
        
    def get_video_duration_moviepy(self, filename):
        """
        Retrieves the duration of a video file using MoviePy.

        Args:
            filename (str): The path to the video file.

        Returns:
            float: The duration of the video in seconds.
        """
        try:
            clip = VideoFileClip(filename)
            duration = clip.duration
            clip.close()  # Release resources
            return duration
        except Exception as e:
            print(f"Error getting video duration with MoviePy: {e}")
            return None

