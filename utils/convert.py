import subprocess
import scipy.io.wavfile as wav
import sys
import numpy as np 
import pyaudio
import time
import wave
from os import path
from pydub import AudioSegment
import pafy  
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_dl import YoutubeDL
dirname = path.dirname(path.dirname(__file__))
sample_rate = 16000


def mp3_to_wav(src):
    try:
        name = src.split('/')[-1].split('.')[0]
        dst = "%s.wav"%(name)
        dst = dirname+'/temp/'+dst
        try:                                                          
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")
            sound = AudioSegment.from_wav(dst)
            sound = sound.set_channels(1)
            sound = sound.set_frame_rate(sample_rate)
            sound.export(dst, format="wav")
            return ("Converted to wav", True)
        except Exception as e:
            print(e)
            return ("Error converting file: "+e,False)
    except Exception as e:
        return (e,False)


def mp4_to_wav(src):
    if src.split('.')[-1] != 'mp4':
        return ('File is not in required format!',False)
    try:
        src = src.split('.mp4')[0]
        command = "ffmpeg -i %s.mp4 -ab 160k -ac 2 -ar 44100 -vn %s.wav"%(src)
        subprocess.call(command, shell=True)
        return ('Complete',True)
    except Exception as e:
        return (e,False)