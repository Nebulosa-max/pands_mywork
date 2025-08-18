import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # <- allowed here per lab instruction

minSalary = 20_000
maxSalary = 80_000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

fig, ax = plt.subplots()

# scatter + x^2
ax.scatter(ages, salaries, label="salaries")
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints
ax.plot(xpoints, ypoints, label="x squared")

# add a KDE “normal-ish” curve for ages on a secondary y-axis
ax2 = ax.twinx()
sns.kdeplot(x=ages, ax=ax2, label="Age KDE")

ax.set_title("Ages vs Salaries + y = x^2 + KDE(ages)")
ax.set_xlabel("x / Age")
ax.set_ylabel("y / Salary")
ax.legend(loc="upper left")
ax2.legend(loc="upper right")
fig.tight_layout()
plt.savefig("q15_scatter_with_kde.png")
plt.show()