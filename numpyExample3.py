import numpy as np
import matplotlib.pyplot as plt
import math

def f1(t):
    return np.cos(t)
def f2(t):
    return np.sin(t)
# evenly sampled time at 200ms intervals
t = np.arange(0., 4*np.pi, 0.2)
#print(t)
# red dashes, blue squares and green triangles
#plt.plot(t, f1(t), 'r--',t, f2(t), 'b--',t, -f1(t), 'g--')
plt.plot(t, f1(t), 'r--',t, -f1(t), 'g--')
plt.show()
