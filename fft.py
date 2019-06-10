import numpy as np
import matplotlib.pyplot as plt


N = 20
x = np.linspace(-3, 3, N)
f = np.exp(-np.square(x))

g = np.fft.fft(f)
k = np.fft.fftfreq(len(f), 6)

plt.figure()
plt.plot(k, np.abs(g))
plt.xlabel('k')
plt.ylabel('g(k)')
plt.show()
