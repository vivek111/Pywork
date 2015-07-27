import numpy as np
import matplotlib.pyplot as plt
t = np.arange(400)
n = np.zeros((400,), dtype=complex)
n[40:60] = np.exp(1j*np.random.uniform(0, 2*np.pi, (20,)))
s = np.fft.fft(n)
#print(s)
plt.plot(t, s.real, 'b-', t, s.imag, 'r--')
plt.legend(('real', 'imaginary'))
plt.show()
