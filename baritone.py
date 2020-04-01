import deepspeech as dp
from deepspeech import Model
import scipy.io.wavfile as wav
import sys
import os
import numpy as np 
import pyaudio
import time
import wave
from .utils import youtube as yt
import requests
from .utils import stt,convert
dirname = os.path.dirname(__file__)


def process_audio(in_data, frame_count, time_info, status):
    global text_so_far
    data16 = np.frombuffer(in_data, dtype=np.int16)
    model.feedAudioContent(context, data16)
    text = model.intermediateDecode(context)
    if text != text_so_far:
        print('Interim text = {}'.format(text))
        text_so_far = text
    return (in_data, pyaudio.paContinue)

def validate_url(url):
	request = requests.get(url)
	if request.status_code == 200:
	    return True
	else:
	    return False

def isYoutube(path):
	return not ('https://www.youtube.com/watch?v=' in path)

def pipeline(path,file_type='local'):
	if file_type == 'youtube':
		if not validate_url(path) or isYoutube(path):
			return ("Page does not exist", False)
		# Need to add function to check validity of youtube url
		# Now checking for captions
		cc,status = yt.get_youtube_cc(path)
		# status = False
		print("Could not get captions")
		if status == True:
			return (cc,True)
		# Else send to voice to text conversion
		print("Retrieving file")
		v_id,status = yt.get_youtube_audio(path)
		if status == False:
			return ("Error: Could not get text: "+str(v_id),False)
		error,status = convert.mp3_to_wav(dirname + '/temp/'+v_id+'.mp3')
		if status == True:
			error,status = stt.speech_to_text(dirname+'/temp/'+v_id+'.wav')
			if status:
				return (error,True)
			else:
				return (error,False)
		else:
			return (error,False)


# print(pipeline("https://www.youtube.com/watch?v=yIdKbSeAueY",'youtube'))

# audio = pyaudio.PyAudio()
# stream = audio.open(
#     format=pyaudio.paInt16,
#     channels=1,
#     rate=16000,
#     input=True,
#     frames_per_buffer=1024,
#     stream_callback=process_audio
# )

# print('Please start speaking, when done press Ctrl-C ...')
# stream.start_stream()

# try: 
#     while stream.is_active():
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     # PyAudio
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
#     print('Finished recording.')
#     # DeepSpeech
#     text = model.finishStream(context)
#     print('Final text = {}'.format(text))