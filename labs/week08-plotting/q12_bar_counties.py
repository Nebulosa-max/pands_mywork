import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ['Mayo','Galway','Roscommon','DirtyDublin','Donegal']
counties = np.random.choice(
    possibleCounties,
    p=[0.10, 0.30, 0.20, 0.12, 0.28],
    size=100
)
unique, counts = np.unique(counties, return_counts=True)

plt.bar(unique, counts)
plt.title("County counts (bar)")
plt.xlabel("County")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("q12_bar_counties.png")
plt.show()