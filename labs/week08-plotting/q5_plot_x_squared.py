import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.savefig("q5_plot_x_squared.png")
plt.show()