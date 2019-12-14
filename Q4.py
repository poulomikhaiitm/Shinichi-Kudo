# Poulomi Kha
# BS16B026
# Comp Bio Assignment2
# Question4


import matplotlib.pyplot as plt 
import numpy as np
t = 300
a = 0.02
b = 0.2
c = -65
d = 6
dt = 0.01
n = int(t/dt)

v = [-70] 
u = [b*v[0]] 
for i in range(1,n):
	if i < int(10/0.01): l = 0
	else : l = 14
	fv = 0.04 * v[i-1] **2 + 5*v[i-1] + 140
	v.append((l + fv - u[i-1] )*dt + v[i-1])
	u.append(( a*(b*v[i-1] - u[i-1]) )*dt + u[i-1])

	if v[i] >= 1 :
		v[i] = c
		u[i] = u[i] + d
plt.title("Izhikevich model	")
plt.plot(v)
plt.ylabel("voltage")
plt.xlabel("time(t/dt)")
plt.legend()
plt.show()