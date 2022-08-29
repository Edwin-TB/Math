# Code to produce a sequence recursively from a recurrence relation

import numpy as np

seed = [1.5,2]
coef = [6,-1]

for i in range (100):
    next = coef[-1]*seed[-1] + coef[-2]*seed[-2]
    seed.append(next)


p = [1, -coef[-1], -coef[-2]]
print(np.poly1d(p))

R = np.roots(p)
print(R)

A = np.array([[R[0]**1,R[1]**1], [R[0]**2, R[1]**2]])
B = np.array([seed[0],seed[1]])
x = np.linalg.solve(A, B)
print(A)
print(B)
print(x)

