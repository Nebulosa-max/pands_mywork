import numpy as np
import matplotlib.pyplot as plt

minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

plt.scatter(ages, salaries)
plt.title("Ages vs Salaries")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("q7_scatter_ages_salaries.png")
plt.show()