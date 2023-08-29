import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation

def fx(x, y, z):
    sig = 10
    return sig * (y - x)

def fy(x, y, z):
    roh = 28
    return x * (roh - z) - y

def fz(x, y, z):
    beta = 8.0 / 3.0
    return x * y - beta * z

nt = 10000
dt = 0.005
x = np.zeros([nt, 1])
y = np.zeros([nt, 1])
z = np.zeros([nt, 1])
time = np.zeros([nt, 1])

x[0] = 0.0
y[0] = 0.01
z[0] = 0.0

for t in range(nt-1):
    x[t+1] = x[t] + dt * fx(x[t], y[t], z[t])
    y[t+1] = y[t] + dt * fy(x[t], y[t], z[t])
    z[t+1] = z[t] + dt * fz(x[t], y[t], z[t])
    time[t+1] = time[t] + dt

## Plotting

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(121, projection='3d')
# Plot the trajectory in 3D
ax.plot(x, y, z)

# Set labels and title
ax.set_xlabel('X', fontsize=14, fontweight='bold')
ax.set_ylabel('Y', fontsize=14, fontweight='bold')
ax.set_zlabel('Z', fontsize=14, fontweight='bold')
ax.set_title('Lorenz Attractor', fontsize=14, fontweight='bold')


# Convert 2D arrays to 1D arrays

x = x.flatten()
y = y.flatten()
z = z.flatten()

# Set up the figure and the 3D subplot

ax = fig.add_subplot(122, projection='3d')

# Set labels and title for the 3D plot
ax.set_xlabel('X', fontsize=14, fontweight='bold')
ax.set_ylabel('Y', fontsize=14, fontweight='bold')
ax.set_zlabel('Z', fontsize=14, fontweight='bold')
ax.set_title('Dynamic Lorenz Attractor', fontsize=14, fontweight='bold')

line, = ax.plot(x, y, z)

def update_plot(i):
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
    return line,

ani = FuncAnimation(fig, update_plot, frames=nt, interval=1)

plt.tight_layout()
plt.show()
