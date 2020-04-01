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


def mp3_to_wav(src,dst = ''):
    try:
        name = src.split('/')[-1].split('.')[0]
        if not dst:
            dst = "%s.wav"%(name)
            dst = dirname+'/temp/'+dst
        try:                                                          
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")
            sound = AudioSegment.from_wav(dst)
            sound = sound.set_channels(1)
            sound = sound.set_frame_rate(sample_rate)
            sound.export(dst, format="wav")
            return (dst, True)
        except Exception as e:
            return ("Error converting file: "+e,False)
    except Exception as e:
        return (e,False)


def mp4_to_wav(src):
    if src.split('.')[-1] != 'mp4':
        return ('File is not in required format!',False)
    try:
        src = src.split('.mp4')[0]
        command = "ffmpeg -i %s.mp4 -ab 160k -ac 1 -ar 16000 -vn %s.wav"%(src)
        subprocess.call(command, shell=True)
        return ('Complete',True)
    except Exception as e:
        return (e,False)

def rectify(path):
    ext =  path.split('.')[-1]
    if ext == 'wav':
        return (path,True)
    elif ext == 'mp3':
        try:
            error, status = mp3_to_wav(path)
            return (error,status)
        except Exception as e:
            return (e,False)
    elif ext == 'mp4':
        return True
