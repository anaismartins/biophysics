from pylab import *
ion()
import fit
from numpy import random, exp
random.seed(0)

def function(params, x):
    """
    set your user defined function
    """
    G0, m = params
    return G0 + m * x

x = []
y = []

# import data
with open("tthermophilus.txt", "r") as f:
    for lines in f:
        data = f.readline()
        x.append(data.split(", ")[0])
        y.append(data.split(", ")[1])

print(x, y)

# No need to provide first guess at parameters for fit.gaus
(xf, yf), params, err, chi = fit.fit(function, x, y)

print("N:    %.2f +/- %.3f" % (params[0], err[0]))
print("N:    %.2f +/- %.3f" % (params[1], err[1]))
print("N:    %.2f +/- %.3f" % (params[2], err[2]))

plot(x,y, 'bo', label='Data')
plot(xf, yf, 'r-', label='Fit')
legend()

