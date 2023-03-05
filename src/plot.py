import matplotlib.pyplot as plt
import numpy as np

from lennard_jones import lennard_jones

epsilon = 1.66e-21
sigma = 3.4e-10

x = np.arange(-0.1, 0.1, 0.001)

plt.plot(x, lennard_jones(x, epsilon, sigma))
plt.xlabel('r')
plt.ylabel('E')
plt.title('Lennard-Jones Potential')
plt.savefig('../results/lennard_jones.png')