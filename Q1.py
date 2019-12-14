# Poulomi Kha
# BS16B026
# Comp Bio Assignment2
# Question1

import matplotlib.pyplot as plt
import numpy as np


r = 10**6
tau = 1
theta = 100
io = 0.18 * 0.001
vt = [0] * 2000
dt = 0.01

for i in range(1,2000):
	vt[i] = vt[i-1] + ((io - vt[i-1]/r)/(tau/r))*dt
	if vt[i] >= theta : vt[i] = 0


plt.title('LIF Q1')
plt.plot(vt)
plt.xlabel('time (t/dt)')
plt.ylabel('voltage')
plt.legend()
plt.show()
