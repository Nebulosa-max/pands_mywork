import numpy as np

minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print(salaries)