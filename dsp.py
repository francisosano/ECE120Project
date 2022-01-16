import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

def note_detect(wav_file):
    wav_file=
    #get the frame rate
    #get the sampling frequency
    file_length=wav_file.getnframes()
    f_s=wav_file.getframerate()
    Sound=np.zeros(file_length)

    print(file_length)
    print(f_s)
    print(Sound)