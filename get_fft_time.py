import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 
from time import time
from scipy import fftpack

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)
samplerate, data = sio.wavfile.read(args.filename)
if data.ndim > 1:
    data = data[:, 0]

print(f"sampling rate: {samplerate}")
print(f"data shape   : {data.shape}")
print(f"data type    : {type(data[0])}")



# Measure time using the code below
###################################
fft = fftpack.fft(data)
magnitude = np.abs(fft)
###################################
