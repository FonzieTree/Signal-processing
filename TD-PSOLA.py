#Charpentier, F.; Stella, M. (Apr 1986). "Diphone synthesis using an overlap-add technique for speech waveforms concatenation". Acoustics, Speech, and Signal Processing, IEEE International Conference on ICASSP'86. 11: 2015–2018. doi:10.1109/ICASSP.1986.1168657
#Author: fangshuming519@gmail.com
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import math
sr, data  = wavfile.read('test.wav', mmap=False)
win = 0.05
num_samples = len(data)
step_size = int(0.5*win*sr)
N = math.ceil(num_samples/step_size)
padding_num = int(N*step_size)-num_samples
data = np.concatenate((data,np.array([0]*padding_num)))
frames = np.zeros((N-1,step_size*2))
#w = 0.5-0.5*np.cos(2*np.pi*(np.arange(-step_size,step_size)+step_size)/(step_size-1))
#w = 0.5-0.5*np.cos(2*np.pi*(np.arange(0,2*step_size))/(2*step_size-1))
#AK Datta, 2017. The Extended Bell Function. Epoch Synchronous Overlap Add (ESOLA): A Concatenative Synthesis Procedure for Speech, page 52.
k1 = 0.125
k2 = 0.875
win_size = step_size * 2
w1 = 0.5-0.5*np.cos(np.pi*(np.arange(0,k1*win_size))/(k1*win_size))
w2 = np.ones(int(((k2-k1)*win_size)))
w3 = 0.5*(1+np.cos(np.pi*(np.arange(k2*win_size,win_size))/(k1*win_size)+np.pi*(2-3*k2)/(k1)))
w = np.concatenate((w1,w2,w3))
#plt.plot(w)
#plt.show()
for i in range(N-1):
    start = step_size*i
    end = step_size*(i+2)
    frames[i] = data[start:end]*w
#special case, ratio = 2
output = np.reshape(frames,newshape=(N-1)*step_size*2,order='C')
output = output.astype(np.int16)
wavfile.write('output.wav', sr, output)
