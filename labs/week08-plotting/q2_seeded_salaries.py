import numpy as np

np.random.seed(1)  # same “random” values each run
minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print(salaries)