import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def f(x, v):
    return v

def g(x, v):
    return -x

nt = 20000
dt = 0.001

x = np.zeros([nt, 1])
v = np.zeros([nt, 1])
time = np.zeros([nt, 1])
v[0] = 0.1

for t in range(nt - 1):
    x[t + 1] = x[t] + dt * f(x[t], v[t])
    v[t + 1] = v[t] + dt * g(x[t], v[t])
    time[t + 1] = time[t] + dt


# Plotting

plt.figure(1, figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, v)
plt.xlabel("Position", fontsize=14, fontweight='bold')
plt.ylabel("Velocity", fontsize=14, fontweight='bold')
plt.title("Phase Space Plot")
plt.gca().set_aspect('equal')

plt.subplot(2, 2, 2)
plt.plot(time, x)
plt.xlabel("Time", fontsize=14, fontweight='bold')
plt.ylabel("Position", fontsize=14, fontweight='bold')
plt.title("Time series - x")

plt.subplot(2, 2, 3)
plt.plot(time, v)
plt.xlabel("Time", fontsize=14, fontweight='bold')
plt.ylabel("Velocity", fontsize=14, fontweight='bold')
plt.title("Time series - v")



# Dynamic phase space plot
ax4 = plt.subplot(2, 2, 4)
plt.xlabel("Position", fontsize=14, fontweight='bold')
plt.ylabel("Velocity", fontsize=14, fontweight='bold')
plt.title("Dynamic Phase Space")
plt.gca().set_aspect('equal')



def update_plot(i):
    ax4.clear()
    ax4.set_xlim(min(x), max(x))
    ax4.set_ylim(min(v), max(v))
    ax4.plot(x[:i], v[:i], '.')
    ax4.set_xlabel("Position", fontsize=14, fontweight='bold')
    ax4.set_ylabel("Velocity", fontsize=14, fontweight='bold')
    ax4.set_title("Dynamic Phase Space")


ani = FuncAnimation(plt.gcf(), update_plot, frames=nt, interval= 1, repeat=False)
plt.tight_layout(pad=1.0)

plt.show()
