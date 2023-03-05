import matplotlib.pyplot as plt
import numpy as np

def lennard_jones(x, epsilon, sigma):
    return 4 * epsilon * (sigma/x**12 - sigma/x**6)


epsilon = 1.66e-21
sigma = 3.4e-10

x = np.arange(0.1, 10, 0.1)

plt.plot(x, lennard_jones(x, epsilon, sigma))
plt.show()