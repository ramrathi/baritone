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


def mp3_to_wav(src):
    try:
        try:
            name = path.split('.')[0]
        except:
            return ('File name error',False)
        dst = "%s.wav"%(name)
        try:                                                          
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")
            return ("Complete",True)
        except:
            return ("Error converting file",False)
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