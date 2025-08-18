import numpy as np
import matplotlib.pyplot as plt

minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.title("Histogram of Salaries")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("q6_hist_salaries.png")
plt.show()