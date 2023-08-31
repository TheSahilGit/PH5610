import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def f(time, x, v):
    return v

def g(time, x, v):
    return -x

nt = 250
#dt = 0.025
dt = 2*np.pi /nt

x = np.zeros([nt, 1])
v = np.zeros([nt, 1])
time = np.zeros([nt, 1])
v[0] = 0.1

for t in range(nt-1):
    k1x = f(time[t], x[t], v[t])
    k1v = g(time[t], x[t], v[t])

    k2x = f(time[t]+0.5*dt, x[t]+0.5*dt*k1x , v[t]+0.5*dt*k1v)
    k2v = g(time[t]+0.5*dt, x[t]+0.5*dt*k1x , v[t]+0.5*dt*k1v)

    k3x = f(time[t]+0.5*dt, x[t]+0.5*dt*k2x , v[t]+0.5*dt*k2v)
    k3v = g(time[t]+0.5*dt, x[t]+0.5*dt*k2x , v[t]+0.5*dt*k2v)

    k4x = f(time[t]+dt, x[t]+dt*k3x , v[t]+dt*k3v)
    k4v = g(time[t]+dt, x[t]+dt*k3x , v[t]+dt*k3v)

    x[t+1] = x[t] + (k1x + 2*k2x + 2*k3x + k4x)*dt/6.0
    v[t+1] = v[t] + (k1v + 2*k2v + 2*k3v + k4v)*dt/6.0
    time[t+1] = time[t] + dt

#---------------------------------------------------------------
#                           Plotting
#---------------------------------------------------------------

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].set_xlabel("Position", fontsize=14, fontweight='bold')
axs[0, 0].set_ylabel("Velocity", fontsize=14, fontweight='bold')
axs[0, 0].set_title("Dynamic Phase Space - Position")
lineP, = axs[0, 0].plot([], [], '-')
axs[0, 0].set_aspect('equal')

axs[0, 1].set_xlabel("Time", fontsize=14, fontweight='bold')
axs[0, 1].set_ylabel("Position", fontsize=14, fontweight='bold')
axs[0, 1].set_title("Dynamic position-time")
lineT, = axs[0, 1].plot([], [], '-')

axs[1, 0].set_xlabel("Position", fontsize=14, fontweight='bold')
axs[1, 0].set_ylabel("Velocity", fontsize=14, fontweight='bold')
axs[1, 0].set_title("Phase Space Plot")
axs[1, 0].set_aspect('equal')
linePV, = axs[1, 0].plot([], [], '-')

axs[1, 1].set_xlabel("Time", fontsize=14, fontweight='bold')
axs[1, 1].set_ylabel("Velocity", fontsize=14, fontweight='bold')
axs[1, 1].set_title("Dynamic velocity-time")
lineV, = axs[1, 1].plot([], [], '-')

def update_plots(i):
    # Update Phase Space - Position subplot
    lineP.set_data(x[:i], v[:i])
    axs[0, 0].set_xlim(min(x)-0.01, max(x)+0.01)
    axs[0, 0].set_ylim(min(v)-0.01, max(v)+0.01)

    # Update Phase Space - Time subplot
    lineT.set_data(time[:i], x[:i])
    axs[0, 1].set_xlim(min(time)-0.01, max(time)+0.01)
    axs[0, 1].set_ylim(min(x)-0.01, max(x)+0.01)

    # Update Dynamic Phase Space - Position subplot
    linePV.set_data(x[:i], v[:i])
    axs[1, 0].set_xlim(min(x)-0.01, max(x)+0.01)
    axs[1, 0].set_ylim(min(v)-0.01, max(v)+0.01)

    # Update Dynamic Phase Space - Time subplot
    lineV.set_data(time[:i], v[:i])
    axs[1, 1].set_xlim(min(time)-0.01, max(time)+0.01)
    axs[1, 1].set_ylim(min(v)-0.01, max(v)+0.01)

ani = FuncAnimation(fig, update_plots, frames=nt, interval=1)
plt.tight_layout(pad=1.0)
plt.show()
