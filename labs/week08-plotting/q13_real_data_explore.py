import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

path = Path("sample.txt")
if path.exists():
    # expects one number per line
    data = np.loadtxt(path, dtype=float)
else:
    # fallback demo data
    data = np.random.normal(loc=50, scale=10, size=200)

plt.hist(data, bins=20)
plt.title("Real-ish data histogram")
plt.tight_layout()
plt.savefig("q13_real_data_hist.png")
plt.show()