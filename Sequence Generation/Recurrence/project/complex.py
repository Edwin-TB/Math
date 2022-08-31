import numpy as np

S = [1,1] # seed numbers
A = [] # array for the calculated first few terms of the sequence
L = 20 # length of A
C = [1,1] # coefficients of terms, ordered in descending power
D = len(C)
p = [1] # characteristic polynomial coefficient array, starts with 1 since that wil always be the coefficient of the highest degree, corresponding to the next entry in the sequence
M = [] # matrix where roots of characteristic polynomial and their powers will be stored
F = [] # array for storing the multiplication functions for each term in the explicit formula
Fc = [] # array for storing symbolic terms of sequence

for i in range (D):
    p.append(-C[i])

R = np.roots(p)
rR = np.real(R)
iR = np.imag(R)
riR = iR * (-i)

for i in range(D):
    M.append([])
    for j in range(D):
        M[i].append(R[j]**(i+1))

E = np.linalg.solve(M, S)
rE = np.real(E)
iE = np.imag(E)
riE = iE * (-i)

for i in range (D):
    F.append(lambda x: E[i]*R[i]**x)

for j in range (L):
    t = 0
    for i in range (D):
        t = t + F[i](j+1)
    A.append(np.round(t, 3))

Fc.append(f'( {rE[0]:0.4g}+{riE[0]:0.4g}i )*( {rR[0]:0.4g}+{riR[0]:0.4g}i )^n')
for i in range(D-1):
    Fc.append(f' + ({rE[i+1]:0.4g} + {riE[i+1]:0.4g}i)*( {rR[i+1]:0.4g} + {riR[i+1]:0.4g}i )^n')
For = ''.join(Fc)
print(A)

""""
print(p)
print(R)
print(M)
print(E)
"""

print(f'The explicit formula for these seed numbers and recurrence coefficients is: \n a_n = {For}')
