import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename)

if data.ndim > 1:
    data = data[:, 0]

times = np.arange(len(data))/float(samplerate)
plt.fill_between(times, data)
plt.xlim(times[0], times[-1])
plt.xlabel('times (s)')
plt.ylabel('amplitude')
plt.show()
