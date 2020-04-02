import deepspeech as dp
from deepspeech import Model
import scipy.io.wavfile as wav
import sys
import os
import numpy as np 
# import pyaudio
import time
import wave
import requests
dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirname)
import utils
import utils.youtube as yt
import utils.database as db

def process_audio(in_data, frame_count, time_info, status):
	global text_so_far
	data16 = np.frombuffer(in_data, dtype=np.int16)
	model.feedAudioContent(context, data16)
	text = model.intermediateDecode(context)
	if text != text_so_far:
		print('Interim text = {}'.format(text))
		text_so_far = text
	return (in_data)

def validate_url(url):
	try:
		request = requests.get(url)
		if request.status_code == 200:
			return True
		else:
			return False
	except:
		return False

def isYoutube(path):
	return not ('https://www.youtube.com/watch?v=' in path)

def pipeline(path,file_type='local'):
	if file_type == 'youtube':
		if not validate_url(path) or isYoutube(path):
			return ("Page does not exist", False)
		# Need to add function to check validity of youtube url
		# Checking in cache
		text,status = db.check_cache(path)
		if(status == True):
			return (text,status)
		# Now checking for captions
		cc,status = yt.get_youtube_cc(path)
		if status == True:
			db.cache(path,cc)
			return (cc,True)
		# Else send to voice to text conversion
		v_id,status = yt.get_youtube_audio(path)
		if status == False:
			return ("Error: Could not get text: "+str(v_id),False)
		error,status = convert.mp3_to_wav(dirname + '/temp/'+v_id+'.mp3')
		if status == True:
			error,status = stt.speech_to_text(dirname+'/temp/'+v_id+'.wav')
			if status:
				text = error
				garbagecollector.dump(dirname + '/temp/'+v_id+'.mp3')
				garbagecollector.dump(dirname+'/temp/'+v_id+'.wav')
				db.cache(path,text)
				return (text,True)
			else:
				return (error,False)
		else:
			return (error,False)
	else:
		if not os.path.isfile(path):
			return ("File does not exist", False)
		try:
			error,status = convert.rectify(path)
			if status == False:
				return (error,status)
			filepath = error
			error,status = stt.speech_to_text(filepath)
			if status:
				return (error,True)
			else:
				return (error,False)
		except Exception as e:
			return (e,False)
		finally: 
			try:
				if 'baritone/temp' in filepath:
					garbagecollector.dump(filepath)
			except:
				print("Problems in main pipeline")






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