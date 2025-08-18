import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0.0, scale=1.0, size=1_000)  # mean 0, std 1
plt.hist(data, bins=30, density=True)
plt.title("Standard Normal random data (μ=0, σ=1)")
plt.tight_layout()
plt.savefig("q14_normalized_random.png")
plt.show()