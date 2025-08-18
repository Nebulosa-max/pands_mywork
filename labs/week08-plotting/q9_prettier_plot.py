# q9_prettier_plot.py
import numpy as np
import matplotlib.pyplot as plt

minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

# base scatter
plt.scatter(ages, salaries, label="salaries")

# y = x^2 overlay (as in Q8)
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints
plt.plot(xpoints, ypoints, label="x squared")

# prettify
plt.title("Ages vs Salaries + y = x^2")
plt.xlabel("x / Age")
plt.ylabel("y / Salary")
plt.legend()
plt.tight_layout()

# Q10: save image
plt.savefig("q9_prettier_plot.png")
plt.show()