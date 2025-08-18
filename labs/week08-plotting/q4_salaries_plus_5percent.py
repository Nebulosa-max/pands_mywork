import numpy as np

np.random.seed(1)
minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesMult = salaries * 1.05          # float array
newSalaries = salariesMult.astype(int)   # convert (floor)
print("orig:", salaries)
print("mult:", newSalaries)