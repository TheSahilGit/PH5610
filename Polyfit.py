import matplotlib.pyplot as plt
import numpy as np

N = 100
x = np.linspace(0.1, 1, N)
y = np.exp(x)

plt.figure(figsize=(10, 10))  # Set the overall figure size

# First subplot
plt.subplot(2, 2, 1)
plt.plot(x, y, color='blue', label='$e^x$')
plt.xlabel("x", fontsize=18)
plt.ylabel("y", fontsize=18)
plt.title("Exponential Function", fontsize=20)
plt.legend(fontsize=16)

# Second subplot with logy scale
plt.subplot(2, 2, 2)
plt.semilogy(x, y, color='red', marker='o', label='$e^x$')
plt.xlabel("x", fontsize=18)
plt.ylabel("y (log scale)", fontsize=18)
plt.title("Exponential Function (Logy Scale)", fontsize=20)
plt.legend(fontsize=16)

# Third subplot showing log(y)
plt.subplot(2, 2, 3)
plt.plot(x, np.log(y), color='red', marker='o', label='$\log(e^x)$')
plt.xlabel("x", fontsize=18)
plt.ylabel("$\log(y)$", fontsize=18)
plt.title("Logarithm of Exponential Function", fontsize=20)
plt.legend(fontsize=16)

# ----------------------------------------------------------------------
# Perform linear regression on the log-log data
log_x = np.log(x)
log_y = np.log(y)
slope, intercept = np.polyfit(x, log_y, 1)

yfit = slope*x + intercept
plt.plot(x, yfit, color='green', marker='.', label='linear fit')
plt.legend(fontsize=16)
# ------------------------------------------------------------------------

# Fourth subplot with linear fit on log-log data
plt.subplot(2, 2, 4)
plt.loglog(x, y, color='blue', marker='o', label='$e^x$')
plt.loglog(x, np.exp(yfit), color='green', linestyle='--', label='Fit: $e^{' + f"{slope:.2f}" + 'x}$')
plt.xlabel("x (log scale)", fontsize=18)
plt.ylabel("y (log scale)", fontsize=18)
plt.title("Exponential Function (Log-Log Scale)", fontsize=20)
plt.legend(fontsize=16)

plt.tight_layout()
plt.show()

print("Slope of the linear fit:", slope)
