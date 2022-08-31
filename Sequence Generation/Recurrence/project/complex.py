import numpy as np

S = [1,1,1] # seed numbers
A = [] # array for the calculated first few terms of the sequence
L = 20 # length of A
C = [1,1,1] # coefficients of terms, ordered in descending power
D = len(C)
p = [1] # characteristic polynomial coefficient array, starts with 1 since that wil always be the coefficient of the highest degree, corresponding to the next entry in the sequence
M = [] # matrix where roots of characteristic polynomial and their powers will be stored
F = [] # array for storing the multiplication functions for each term in the explicit formula
Fc = [] # array for storing symbolic terms of sequence

for i in range (D):
    p.append(-C[i])

R = np.roots(p)
rR = np.real(R)
iR = np.imag(R) * (-i)

for i in range(D):
    M.append([])
    for j in range(D):
        M[i].append(R[j]**(i+1))

E = np.linalg.solve(M, S)
rE = np.real(E)
iE = np.imag(E) * (-i)

for i in range (D):
    F.append(lambda x: E[i]*R[i]**x) ## The function!!!

for j in range (L):
    t = 0
    for i in range (D):
        t = t + F[i](j+1)
    A.append(np.round(t, 3))

if iR.all == 0:
    Fc.append(f'({rE[0]:0.4g})*({rR[0]:0.4g})^n')
    for i in range(D-1):
        Fc.append(f' + ({rE[i+1]:0.4g})*({rR[i+1]:0.4g})^n')
else:
    if iR[0] == 0:
        Fc.append(f'({rE[0]:0.4g})*({rR[0]:0.4g})^n')
    else:
        Fc.append(f'({rE[0]:0.4g} + {iE[0]:0.4g}i)*({rR[0]:0.4g} + {iR[0]:0.4g}i)^n')
    for i in range(D-1):
        if iR[i+1] == 0:
            Fc.append(f' + ({rE[i+1]:0.4g})*({rR[i+1]:0.4g})^n')
        else:
            Fc.append(f' + ({rE[i+1]:0.4g} + {iE[i+1]:0.4g}i)*({rR[i+1]:0.4g} + {iR[i+1]:0.4g}i)^n')


For = ''.join(Fc)
print(A)
print(R)

""""
print(p)
print(R)
print(M)
print(E)
"""

print(f'The explicit formula for these seed numbers and recurrence coefficients is: \n a_n = {For}')
