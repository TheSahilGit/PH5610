import matplotlib.pyplot as plt
import numpy as np


g = 9.8
nt = 20
dt = 1

x = np.zeros([nt, 1])
y = np.zeros([nt, 1])
vx = np.zeros([nt, 1])
vy = np.zeros([nt, 1])
time = np.zeros([nt, 1])


theta = np.pi/4.0
v0 = 10

x[0] = 0
y[0] = 0
vx[0] = v0 * np.cos(theta)
vy[0] = v0 * np.sin(theta)



for t in range(nt - 1):
    x[t + 1] = x[t] + dt * vx[t]
    y[t + 1] = y[t] + dt * vy[t]
    vx[t + 1] = vx[t] + dt * 0
    vy[t + 1] = vy[t] + dt * (-g)
    time[t + 1] = time[t] + dt


# Analytic solution

A = -g/(2*v0**2 * np.cos(theta)**2)

xx = np.linspace(0,nt,nt+1)
yy = A*np.multiply(xx,xx) + np.tan(theta)*xx

print(xx)

plt.plot(x,y)
plt.plot(xx,yy)
#plt.gca().set_aspect('equal')
plt.show()


