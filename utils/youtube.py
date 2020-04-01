import subprocess
import scipy.io.wavfile as wav
import sys
import numpy as np 
import pyaudio
import time
import wave
import os
from pydub import AudioSegment
import pafy  
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_dl import YoutubeDL


def get_youtube_cc(url):
    try:
        video_ids = [url.split('?v=')[1]]
        id = video_ids[0]
        captions = str()
        cc = (YouTubeTranscriptApi.get_transcripts(video_ids, languages=['de', 'en']))
        for line in (cc[0][id]):
           captions+=(' '+line['text'])
        return (captions,True)
    except Exception as e:
        return ("Can't fetch from youtube captions",False)

def get_youtube_audio(url):
    try:
        dirname = os.path.dirname(os.path.dirname(__file__))
        video_ids = [url.split('?v=')[1]]
        id = video_ids[0]
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': dirname+'/temp/%(id)s.%(etx)s',
        'quiet': False
        }
        ydl = YoutubeDL(ydl_opts)
        ydl.download(video_ids)
        return (id,True)
    except Exception as e:
        return (e,False)




