import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation


n = 500

theta = np.linspace(0, 2*np.pi, n)
y = np.sin(theta) #+ 2 * np.sin(3*theta) + 2 * np.sin(10*theta)



# Static Plot
plt.subplot(1,2,1)
plt.plot(y)
plt.xlabel("Position", fontsize=14, fontweight='bold')
plt.ylabel("Velocity", fontsize=14, fontweight='bold')
plt.title("Static Plot", fontsize=14, fontweight='bold')


# Dynamic plot
ax4 = plt.subplot(1,2,2)
def update_plot(i):
    ax4.clear()
    ax4.set_xlim(min(theta), max(theta))
    ax4.set_ylim(min(y), max(y))
    ax4.plot(theta[:i], y[:i], '-')
    plt.xlabel("Position", fontsize=14, fontweight='bold')
    plt.ylabel("Velocity", fontsize=14, fontweight='bold')
    plt.title("Dynamic Plot", fontsize=14, fontweight='bold')

ani = FuncAnimation(plt.gcf(), update_plot, frames=n, interval= 1, repeat=True)
plt.tight_layout(pad=1.0)

plt.show()
