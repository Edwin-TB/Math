import numpy as np

#setup variables
S = [1] # seed numbers
C = [1] # coefficients of terms, ordered in descending power

def generate_formula(seed, coeff):

    D = len(coeff)
    p = [1] # characteristic polynomial coefficient array, starts with 1 since that wil always be the coefficient of the highest degree, corresponding to the next entry in the sequence
    M = [] # matrix where roots of characteristic polynomial and their powers will be stored
    F = [] # array for storing the multiplication functions for each term in the explicit formula
    
    for i in range (D): # creates polynomial
        p.append(-coeff[i])

    R = np.roots(p) # an array with the characteristic roots of the polynomial

    for i in range(D): # function that creates a matrix with the roots taken to their respective powers
        M.append([]) # creates a row in the matrix
        for j in range(D):
            M[i].append(R[j]**(i+1)) # for each row in the matrix, adds the roots to the respective power

    E = np.linalg.solve(M, seed) # solves for the solution to the matrix and seed numbers to get coefficients

    for i in range (D):
        F.append(lambda x: E[i]*(R[i]**x)) ## The function!!! adds the coefficient/root pair to the function

    Fc = [] # array for storing symbolic terms of sequence
    A = [] # array for the calculated first few terms of the sequence
    L = 20 # length of A

    rR = np.real(R) # an array with all the real parts of the roots
    iR = np.imag(R) # an array with all the imaginary parts of the roots
    rE = np.real(E) # real parts of each coefficient
    iE = np.imag(E) # imaginary parts of each coefficient

    for j in range (L):
        t = 0
        for i in range (D):
            t = t + F[i](j+1) # adds each term in the function and appends it to the display array A
        A.append(np.round(t, 3))

    if iR.all == 0:
        Fc.append(f'({rE[0]:0.4g})*({rR[0]:0.4g})^n') # adds the first element in the function if the roots of the characteristic polynomial are all real
        for i in range(D-1): # -1 to adjust for initial term
            Fc.append(f' + ({rE[i+1]:0.4g})*({rR[i+1]:0.4g})^n') # +1 to adjust for initial term
    else:
        if iR[0] == 0:
            Fc.append(f'({rE[0]:0.4g})*({rR[0]:0.4g})^n') # adds initial term
        else:
            Fc.append(f'({rE[0]:0.4g} + {iE[0]:0.4g}i)*({rR[0]:0.4g} + {iR[0]:0.4g}i)^n') # adds initial term
        for i in range(D-1):
            if iR[i+1] == 0: # conditional accounts for 0 roots
                Fc.append(f' + ({rE[i+1]:0.4g})*({rR[i+1]:0.4g})^n') # adds succesive terms
            else:
                Fc.append(f' + ({rE[i+1]:0.4g} + {iE[i+1]:0.4g}i)*({rR[i+1]:0.4g} + {iR[i+1]:0.4g}i)^n') # adds successive terms

    For = ''.join(Fc) # creates string containing each term in the formula

    return R, E, A, For

for i in range(6):
    S.pop(-1)
    S.append(0)
    S.append(1)
    C.append(1)
    ratio = str(np.round(generate_formula(S, C)[0][0], 12))
    r = ratio.translate({ord(i): None for i in '()+j'})[:-1]
    print(r)
    print(generate_formula(S, C)[-1])

# print(f'The explicit formula for these seed numbers and recurrence coefficients is: \n a_n = {For}')
