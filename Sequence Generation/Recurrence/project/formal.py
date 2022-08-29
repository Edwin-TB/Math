import numpy as np

# the 'seed' numbers of a sequence are the first few terms, the number of seed numbers is the degree of the sequence
S = [1.5,2]
D = len(S)

# the coefficients are just that, the coefficients attached to the seed numbers in a sequence
C = [6,-1]
print(f'The recurrence relation with these coefficients is: \n A(n) = {C[-1]}A(n-1) + {C[-2]}A(n-2) \n')

# the Vinton function will calculate the first few terms of each sequence for later when comparison is required to prove a result. 'Few' means the degree times 2
for i in range (D):
    R = C[-1]*S[-1] + C[-2]*S[-2]
    S.append(R)

# to generate the characteristic polynomial of the relation, the highest degree is the output itself with coefficient 1
# the following coefficients are the coefficients of the next highest terms and negative since they were subtracted from the other side 
p = [1, -C[-1], -C[-2]]
print(f'The characteristic polynomial of this recurrence relation is: \n {np.poly1d(p)} \n')

R = np.roots(p)
print(f'The roots of this characteristic polynomial are: \n R1 = {R[0]:0.3g}; R1 = {R[1]:0.3g} \n')

print('The system we now want to solve is given by: \n A1 = C1*R1^1 + C2*R2^1 \n A2 = C1*R1^2 + C2*R2^2')
print(f'Plugging in the seeds and roots obtained we get: \n {S[0]} = C1*{R[0]:0.3g}^1 + C2*{R[1]:0.3g}^1 \n {S[1]} = C1*{R[0]:0.3g}^2 + C2*{R[1]:0.3g}^2')

A = np.array([[R[0]**1,R[1]**1], [R[0]**2, R[1]**2]])
B = np.array([S[0],S[1]])
x = np.linalg.solve(A, B)

print(A)
print(B)
print(x)

