from src.review_extractor.main import handler

if __name__ == "__main__":
    event = {
        "Records": [
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-08-02/1401005479341068388_Untitled_video_-_Made_with_Clipchamp.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-08-01/1400901194049655005_New_World_2025.08.01_-_02.00.13.05.DVR_-_Trim_-_Trim_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-08-01/1400722197915369492_New_World_2025.08.01_-_01.53.29.02.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-08-01/1400666953718435961_spin2win_-_Made_with_Clipchamp.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-08-01/1400657820751233178_grav_well_-_Made_with_Clipchamp.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-31/1400543072667963547_lord_nerd2.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-31/1400542812491223173_lord_nerd2.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-31/1400542812491223173_lord_nerd_3.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-31/1400335006303522868_gate_spin.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-31/1400330255025045566_naked_2.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-31/1400329474326790184_Naked_and_Afraid.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1400153398665285652_Creedboots-exe.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399962085147807864_New_World_2025.02.15_-_10.04.59.02.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399961542648402022_Brawl_2.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399961374985027634_Brawl_3.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399961034495627335_Choke_8.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399960921769513080_Wall_push.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399960770506391554_Massacre.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399960468105203733_1v3_Carry.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399957726192341084_Fair_Fight.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399954004745912320_4.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399951868909846659_Speed_15.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399931358943379476_New_World-_Aeternum_-_2025-07-28_3-31-42_PM.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-30/1399915316989136916_Moments-clip-from-Jul-29-2025.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-29/1399902332937830502_New_World_2025.07.29_-_19.33.12.14.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-29/1399902315791781949_New_World_2025.07.29_-_18.39.25.12.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-28/1399267786852794439_New_World_2025.07.28_-_00.40.11.02.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-26/1398537100311265352_New_World_2025.07.26_-_01.17.45.04.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-26/1398534154370551821_New_World_2025.07.26_-_01.03.12.02.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-26/1398533765722013816_New_World_2025.07.26_-_01.07.53.03.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-25/1398434384293396540_New_World_2025.07.20_-_00.52.11.08.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-25/1398157254229753927_New_World_2025.07.24_-_23.34.10.06.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-25/1398144892139606156_New_World_2025.07.22_-_23.46.02.09.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-25/1398143881148629143_New_World_2025.07.23_-_19.56.19.02.DVR.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-25/1398135636959039569_New_World_2025.07.24_-_22.08.19.04.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-25/1398135223572758588_New_World_2025.07.24_-_22.37.32.05.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-25/1398106009142169741_New_World_2025.07.24_-_20.22.16.02.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-24/1398048041306427463_Faith1.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-24/1398038435973042317_turn_around.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-24/1397732147464507423_MedalTVNewWorld20250723191128-1753313552.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-24/1397731909030777005_Nail_Biter_4.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-24/1397730657660174520_New_World_2025.07.23_-_19.56.19.02.DVR.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-23/1397724745482633306_JACK_2.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-23/1397724508474839130_kobe.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-23/1397724167108821174_clip_13.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-23/1397724162709000222_kKmhLTcGMXSBtQXfq.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397285179508396183_New_World_2025-07-22_14-24-00.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397090724377268254_New_World_2025.07.22_-_01.29.18.07.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397074801339793439_kHs0DCixzA96H_cIB.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397074598671028224_kJUM5HoHtbSl4Ovu1.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397037857419431936_New_World_2025.07.21_-_21.19.41.03.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397037849756434463_New_World_2025.07.21_-_21.07.14.02.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397021466578391081_clip_10.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397021326811725834_clip_8.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397021214697848873_clip_7.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397021135115259984_clip_6.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397020894123003964_clip_5.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-22/1397020812472488056_clip_3.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396730008130682900_New_World_2025.06.20_-_14.10.50.02.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396729958684164206_New_World_2025.06.18_-_23.39.36.11.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396729767159398481_New_World_2025.06.18_-_22.01.36.05.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396729752298983485_New_World_2025.06.18_-_22.09.28.06.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396729728483983460_New_World_2025.06.16_-_21.34.02.03.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396729709316018277_New_World_2025.06.10_-_15.42.20.02.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396729683609124934_New_World_2025.05.24_-_14.16.44.05.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396729655968665610_ecfc5c39-fc1f-49c0-a32e-ff0ab7ac07ed.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396720581558272092_Auto-clip-Reaction-clipping.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396713963156275310_New_World_2025.07.19_-_21.42.56.02.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396713806104629310_New_World_2025.06.19_-_22.06.07.02.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396713795736571904_New_World_2025.06.15_-_15.33.13.05.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396713783262445658_New_World_2025.06.13_-_22.25.59.03.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396713768951484416_New_World_2025.06.13_-_22.15.32.02.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396713758025580726_New_World_2025.05.31_-_21.12.00.06.DVR_-_Trim.mov"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396710832762654870_New_World_2025.07.18_-_00.09.45.07.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396710474892050544_New_World_2025.07.19_-_00.08.11.03.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396677684670763008_Ass_ran_over.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396677411202011176_Moments-clip-from-Jul-20-2025.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396677382970282035_Apprehended.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396676088641486889_New_World_2025.02.08_-_00.05.06.16.DVR_-_Trim.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396674570035003425_VidxUpload3MusketSpikeOPR.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396673620079542422_VidxUpload2MusketSpikeOPR.mp4"
      }
    }
  },
  {
    "s3": {
      "bucket": {
        "name": "vidx-clip-videos"
      },
      "object": {
        "key": "1287543971438002238/2025-07-21/1396671156244713565_VidxUpload1MusketSpikeOPR.mp4"
      }
    }
  }
]
        }

    handler(event, {})
    
    prompts = [
        {            "prompt_name": "transcribe audio",
            "prompt_content": "Can you transcribe the audio on this video and give me all the audio output in text"
        },
        {            "prompt_name": "sentiment_analysis",
            "prompt_content": "Task: You are an expert at analyzing video and audio to extract moments of excitement and sentiment. Given an audio or video segment, carefully review the audio to detect signs of excitement or high-intensity moments. Consider as excitement: -Shouting -Laughing -Cheering -Crowd noise -Celebration sounds (e.g., applause, goal, win, victory sounds) -Sudden increase in loudness or pitch If you find any excitement or intense moment, identify the exact timestamp (in seconds or mm:ss) where it occurs, and explain the reason for your judgment. If there is no excitement present, return 'neutral' as sentiment, and explain briefly. Your response must be a JSON object with these fields: sentiment: 'excited' or 'neutral' reason: Short explanation of your judgment (e.g., 'cheering and laughter detected at 01:23') timestamp: Timestamp of excitement (if any), or null if neutral"
        },
        {            "prompt_name": "metadata",
            "prompt_content": "summarize the video, generate hashtags, and find the category of the video. Categories are: 1 **world pvp** - Usually out in the open field where there are between 2-20 allies engaging in combat with enemies. 2 **OPR** - Instance player vs player where a team of exactly 5 fights against other groups of players. 3 **Arena** - team of 3 allies fighting against a team of 3 enemies in a closed arena. 4 **Clutch pvp** - One player by himself is able to fight and defeat multiple opponents. The output should be a json object containing **description**, **category**, **hashtags**"
        },
        {            "prompt_name": "video_highlights",
            "prompt_content": "What are the highlights of this video? What are the most important moments?"
        }
    ]
