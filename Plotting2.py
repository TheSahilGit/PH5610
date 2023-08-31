import matplotlib.pyplot as plt
import numpy as np

 
N = 100

x = np.linspace(0,2*np.pi,N)
y1 = np.sin(x)
y2 = np.cos(x)




## Enable LaTeX rendering
plt.rcParams['text.usetex'] = True

plt.plot(x,y1, label = '$ \\sin(x) $', color = 'blue', marker='o', markersize=5, linestyle='-.', linewidth=2)
plt.plot(x,y2, label = '$ \\cos(x) $', color = 'green', marker='s', markersize=5, linestyle='--', linewidth=2)

plt.xlabel("$x$", fontsize=28, fontweight='bold')
plt.ylabel("$y$", fontsize=28, fontweight='bold')
plt.title("$ \\textbf{ Basic plotting} $", fontsize=26, fontweight='bold')

x_tick_positions = np.linspace(0, 2*np.pi, 5)  # Choose the number of ticks you want
#x_tick_labels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
x_tick_labels = ["$0$", "$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{3 \\pi}{2}$", "$2 \\pi $"]

plt.xticks(x_tick_positions, x_tick_labels, fontsize=18)

plt.legend(fontsize=24)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)

#plt.gca().set_aspect('equal')

plt.show()