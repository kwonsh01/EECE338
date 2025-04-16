import argparse
import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt



parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()


print("drawing fft plot for", args.filename)
samplerate, data = sio.wavfile.read(args.filename)
if data.ndim > 1:
    data = data[:, 0]

print(f"sampling rate: {samplerate}")
print(f"data shape   : {data.shape}")


T = int(len(data)/samplerate)
print(f"record time  : {T} [s]")


d_fft = np.fft.fft(data)
amplitude = abs(d_fft)*(2/len(d_fft))
frequency = np.fft.fftfreq(len(d_fft), 1/samplerate)


plt.stem(frequency[:int(len(amplitude)/2)], amplitude[:int(len(amplitude)/2)])
plt.grid(True)
plt.show()
