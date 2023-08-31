import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)  # Set seed for reproducibility
data = np.random.rand(1000)
#data = np.random.rand(1000) # Gaussian


# Write data to a file
data_file = 'random_data.txt'
np.savetxt(data_file, data)

# Read data from the file
read_data = np.loadtxt(data_file)


# Plot the data
plt.subplot(1,2,1)
plt.plot(read_data, marker='o')
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Random Data Plot")

plt.subplot(1,2,2)
plt.hist(read_data, bins=20, edgecolor='black')  # bins specify the number of bins in the histogram
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Random Data")
plt.show()
plt.show()
