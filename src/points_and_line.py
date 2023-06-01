import matplotlib.pyplot as plt
import numpy as np

from nbuck import nbuck

force = []
np = []
np_error = []

with open("../data/buckling.txt") as file:
    for line in file:
        strline = file.readline()
        force.append(strline.split()[0])
        np.append(strline.split()[1])
        np_error.append(strline.split()[2])

plt.plot(x, nbuck(force, L = 21000 * 0.34, C = 110, A = 45))
plt.xlabel('Force (pN)')
plt.ylabel('n_B')
plt.title('Buckling')
plt.savefig('../results/buckling.png')