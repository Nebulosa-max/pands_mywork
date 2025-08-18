import numpy as np

np.random.seed(1)
minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5_000
print("orig:", salaries)
print("plus:", salariesPlus)
