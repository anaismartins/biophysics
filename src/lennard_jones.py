def lennard_jones(x, epsilon, sigma):
    return 4 * epsilon * (sigma/x**12 - sigma/x**6)