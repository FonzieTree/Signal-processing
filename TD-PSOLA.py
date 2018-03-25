#Charpentier, F.; Stella, M. (Apr 1986). "Diphone synthesis using an overlap-add technique for speech waveforms concatenation". Acoustics, Speech, and Signal Processing, IEEE International Conference on ICASSP'86. 11: 2015–2018. doi:10.1109/ICASSP.1986.1168657
#Author:fangshuming519@gmail.com
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import math
sr, data  = wavfile.read('test.wav', mmap=False)
win = 0.02
num_samples = len(data)
step_size = int(0.5*win*sr)
N = math.ceil(num_samples/step_size)
padding_num = int(N*step_size)-num_samples
data = np.concatenate((data,np.array([0]*padding_num)))
frames = np.zeros((N-1,step_size*2))
w = 0.5-0.5*np.cos(2*np.pi*np.arange(0,2*step_size)/(2*step_size))
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
