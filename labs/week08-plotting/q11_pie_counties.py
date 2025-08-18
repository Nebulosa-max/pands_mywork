import numpy as np
import matplotlib.pyplot as plt

# make a long list (with some counties more frequent)
possibleCounties = ['Mayo','Galway','Roscommon','DirtyDublin','Donegal']
counties = np.random.choice(
    possibleCounties,
    p=[0.10, 0.30, 0.20, 0.12, 0.28],
    size=100
)

unique, counts = np.unique(counties, return_counts=True)

plt.pie(counts, labels=unique)
plt.title("County mix (pie)")
plt.tight_layout()
plt.savefig("q11_pie_counties.png")
plt.show()