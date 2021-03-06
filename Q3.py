# Poulomi Kha
# BS16B026
# Comp Bio Assignment2
# Question3

import matplotlib.pyplot as plt
import numpy as np

r = 10**6
tau = 1
theta = 100
tref = 2
dt = 0.01
io = list(np.arange((theta/r)+10**-8, 8*10**-4, 10**-6))
f = [0] * 700

for i in range(700):
	f[i] = 1/(np.log(r*io[i]/(r*io[i]-theta))*tau+tref)

plt.title('LIF Q3')
plt.plot(io,f)
plt.xlabel('I(Amperes)')
plt.ylabel('Frequency(Hz)')
plt.legend()
plt.show()