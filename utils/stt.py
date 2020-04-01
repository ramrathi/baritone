from deepspeech import Model
import scipy.io.wavfile as wav
import sys
import os
import wave
sample_rate = 16000
beam_width = 500
lm_alpha = 0.75
lm_beta = 1.85
n_features = 26
n_context = 9

dirname = os.path.dirname(os.path.dirname(__file__))
model_name = dirname+"/models/output_graph.pbmm"
alphabet = dirname+"/models/alphabet.txt"
langauage_model = dirname+"/models/lm.binary"
trie = dirname+"/models/trie"

# ds = Model(dirname+'/models/output_graph.pbmm',500)
ds = Model(model_name,beam_width)
try:
	ds.enableDecoderWithLM(langauage_model, trie, lm_alpha, lm_beta)
except:
	print("No language model and trie specified")

def downsampleWav(src, dst, inrate=44100, outrate=sample_rate, inchannels=2, outchannels=1):
    if not os.path.exists(src):
        print('Source not found!')
        return False

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    try:
        s_read = wave.open(src, 'r')
        s_write = wave.open(dst, 'w')
    except Exception as e:
        print(e)
        print('Failed to open files!')
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
    except:
        print('Failed to downsample wav')
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except:
        print('Failed to write wav')
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print ('Failed to close wav files')
        return False

    return True

def speech_to_text(path):
	print(path)
	if os.path.isfile(path):
		try:
			fs, audio = wav.read(path)
			processed_data = ds.stt(audio)
			print(processed_data)
			return (processed_data,True)	
		except Exception as e:
			print(e)
			return(e,False)
	else:
		print("dasf")
		return ("File not found error: "+path,False)
	
