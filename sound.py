import os
import wave
import pyaudio

import config

WAVE     = None
MOVE     = wave.open(os.path.join(config.RESOURCES_DIR, 'press_02.wav'),    'rb')
OUTBOUND = wave.open(os.path.join(config.RESOURCES_DIR, 'outbound_01.wav'), 'rb')
MATCH    = wave.open(os.path.join(config.RESOURCES_DIR, 'match_01.wav'),    'rb')
UNMATCH  = wave.open(os.path.join(config.RESOURCES_DIR, 'unmatch_01.wav'),  'rb')
WIN      = wave.open(os.path.join(config.RESOURCES_DIR, 'win_01.wav'),      'rb')

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
	data = WAVE.readframes(frame_count)
	return (data, pyaudio.paContinue)
