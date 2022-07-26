# OS used/Python Version: Ubuntu (CSE VM 3.1.2) using Python 3.8.10

# How to run: python3 QR-Decomposition.py

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

A = np.array([
    [1, 0, 4],
    [-2, 3, -2],
    [-2, 0, 6]
])

print("Matrix A")
print(A)

# A = Q R
# q is the orthonormalized vectors
# r is upper-triangular vectors
# https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.linalg.qr.html#scipy.linalg.qr
q, r = linalg.qr(A)

print("Matrix Q")
print(q)

print("Matrix R")
print(r)

# Q and R are slightly off to their true solutions due to floating point representation (rounding errors)
# when we try to use QR = A to verify our results
