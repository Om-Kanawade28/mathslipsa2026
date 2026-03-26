import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random numbers between 0 and 100
numbers = np.random.randint(0, 100, 100)

# Draw histogram
plt.hist(numbers, bins=10)

# Labels and title
plt.title("Histogram of 100 Random Numbers (NumPy)")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show plot
plt.show()