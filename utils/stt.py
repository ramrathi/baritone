from deepspeech import Model
import scipy.io.wavfile as wav
import sys
import os.path

ds = Model('../models/output_graph.pbmm',500)

def speech_to_text(path):
	if os.path.isfile(path):
		try:
			fs, audio = wav.read(path)
			print(fs)
			processed_data = ds.stt(audio)
			return (processed_data,True)	
		except Exception as e:
			return(e,False)
	else:
	    return ("File not found error: "+path,False)
	

