import matplotlib.pyplot as plt
import numpy as np

N = 100
x = np.linspace(0.01, 1, N)
y = np.exp(x)



plt.figure(figsize=(10, 5))  # Set the overall figure size

# First subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='blue', label='$e^x$')  # Specify color and label
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.title("Exponential Function", fontsize=16)
plt.legend()  # Display legend

# Second subplot with log-log scale
plt.subplot(1, 2, 2)
plt.semilogy(x, y, color='red', marker='o', label='$e^x$')  # Use loglog() and add markers
plt.xlabel("x (log scale)", fontsize=14)
plt.ylabel("y (log scale)", fontsize=14)
plt.title("Exponential Function (Log-Log Scale)", fontsize=16)
plt.legend()  # Display legend

plt.tight_layout()  # Ensure subplots don't overlap
plt.show()
