import matplotlib.pyplot as plt
import numpy as np 

theta = np.linspace(0, 2*np.pi, 100)
y = np.sin(theta)

plt.plot(y)
plt.show()
