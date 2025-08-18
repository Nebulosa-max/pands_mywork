import numpy as np
import matplotlib.pyplot as plt

minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

plt.scatter(ages, salaries, label="Ages vs Salaries")

# y = x^2 line (independent illustrative curve)
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints
plt.plot(xpoints, ypoints, label="y = x^2")

plt.title("Ages vs Salaries + y = x^2")
plt.xlabel("x / Age")
plt.ylabel("y / Salary")
plt.legend()
plt.tight_layout()
plt.savefig("q8_scatter_plus_x_squared.png")
plt.show()