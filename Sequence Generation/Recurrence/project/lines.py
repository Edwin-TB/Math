import numpy as np 
import matplotlib.pyplot as plt

S = [1,1,1,1,1,1,1,1,1,1,1,1] # seed numbers
C = [1,1,1,1,1,1,1,1,1,1,1,1] # coefficients of terms, ordered in descending power
D = len(C)
p = [1] # characteristic polynomial coefficient array, starts with 1 since that wil always be the coefficient of the highest degree, corresponding to the next entry in the sequence

for i in range (D):
    p.append(-C[i])

R = np.roots(p)

ratio = np.amax(R)

T = [1]
for i in range (D):
    term = T[-1]/ratio
    T.append(np.round(term.real, 3))

print(T)
X = []
for x in T:
    X.append(1)

plt.scatter(X, T)
plt.show()