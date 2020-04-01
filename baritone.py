import deepspeech as dp
from deepspeech import Model
import scipy.io.wavfile as wav
import sys
import os
import numpy as np 
import pyaudio
import time
import wave

# def process_audio(in_data, frame_count, time_info, status):
#     global text_so_far
#     data16 = np.frombuffer(in_data, dtype=np.int16)
#     model.feedAudioContent(context, data16)
#     text = model.intermediateDecode(context)
#     if text != text_so_far:
#         print('Interim text = {}'.format(text))
#         text_so_far = text
#     return (in_data, pyaudio.paContinue)

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