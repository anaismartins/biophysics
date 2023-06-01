from numpy import pi, sqrt

kBT = 4 # pN nm

def nbuck(force, L, C, A):
    return L / (C * pi) * sqrt(A * force / (2 * kBT))