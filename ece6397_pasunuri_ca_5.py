#header
"""module for portion"""
import time as t
import numpy as np
import portion as por
import ece6397_pasunuri_helper_headerfooter as h
ca1=h.Header("Aravind Reddy","Pasunuri","Assignment 5","Data Estimation")
for i in range(2):
    ca1.horizontal_line()
ca1.student_name()
ca1.ca_name()
ca1.horizontal_line()
ca1.description()
Start_time=t.time()
print("START RUN")
ca1.horizontal_line()
class Port:
    """class for intevals"""
    def __init__(self):
        pass
    def addition(self, a_a,b_a):
        """for addition"""
        c_a=por.closed((a_a.lower+b_a.lower),(a_a.upper+b_a.upper))
        return c_a
    def subtraction(self,a_s,b_s):
        """for subtraction"""
        c_s=por.closed((a_s.lower-b_s.upper),(a_s.upper-b_s.lower))
        return c_s
    def multiplication(self,a_m,b_m):
        """for multiplication"""
        k_m=[]
        k_m.extend([a_m.lower*b_m.lower,a_m.lower*b_m.upper])
        k_m.extend([a_m.upper*b_m.lower,a_m.upper*b_m.upper])
        m_m=por.closed(min(k_m),max(k_m))
        return m_m
    def reciprocal(self,a_r):
        """for reciprocal"""
        c_r=por.closed(1/a_r.upper,a_r.lower)
        return c_r
    def division(self,a_d,b_d):
        """for division"""
        c_d=self.multiplication(a_d,self.reciprocal(b_d))
        return c_d
    def maxnmin(self,a_max,b_max):
        """for maximum"""
        l_max=[]
        l_max.extend([a_max.lower,b_max.lower])
        k_max=[]
        k_max.extend([a_max.upper,b_max.upper])
        c_max=por.closed(max(l_max),max(k_max))
        return c_max
    def minimum(self,a_min,b_min):
        """for minimum"""
        l_min=[]
        l_min.extend([a_min.lower,b_min.lower])
        k_min=[]
        k_min.extend([a_min.upper,b_min.upper])
        c_min=por.closed(min(l_min),min(k_min))
        return c_min
K=Port()
A=np.empty((8,6),dtype=object)

A[0][0]=por.closed(0,0)
A[0][1]=por.closed(0,0)
A[0][2]=por.closed(0,0)
A[0][3]=por.closed(-3,-1)
A[0][4]=por.closed(0,0)
A[0][5]=por.closed(0,0)

A[1][0]=por.closed(-2,-1)
A[1][1]=por.closed(0,0)
A[1][2]=por.closed(0,0)
A[1][3]=por.closed(-3,-2)
A[1][4]=por.closed(-3,-1)
A[1][5]=por.closed(0,0)

A[2][1]=por.closed(-2,-1)
A[2][0]=por.closed(-3,-2)
A[2][2]=por.closed(0,0)
A[2][4]=por.closed(-3,-2)
A[2][5]=por.closed(-3,-1)
A[2][3]=por.closed(-4,-3)

A[3][2]=por.closed(-2,-1)
A[3][1]=por.closed(-3,-2)
A[3][0]=por.closed(-3.5,-2)
A[3][5]=por.closed(-3,-2)
A[3][3]=por.closed(-6,-4)
A[3][4]=por.closed(-4,-3)

A[4][0]=por.closed(-4,-2.25)
A[4][1]=por.closed(-3.5,-2)
A[4][2]=por.closed(-3,-2)
A[4][3]=por.closed(-5,-4)
A[4][4]=por.closed(-6,-4)
A[4][5]=por.closed(-4,-3)

A[5][0]=por.closed(-3.5,-2)
A[5][1]=por.closed(-4,-2.25)
A[5][2]=por.closed(-3.5,-2)
A[5][3]=por.closed(-4.5,-4)
A[5][4]=por.closed(-5,-4)
A[5][5]=por.closed(-6,-4)

A[6][0]=por.closed(-2,-1.25)
A[6][1]=por.closed(-3.5,-2)
A[6][2]=por.closed(-4,-2.25)
A[6][3]=por.closed(-5.5,-5)
A[6][4]=por.closed(-4.5,-4)
A[6][5]=por.closed(-5,-4)

A[7][0]=por.closed(-2,-1.5)
A[7][1]=por.closed(-2,-1.25)
A[7][2]=por.closed(-3.5,-2)
A[7][3]=por.closed(-6,-5)
A[7][4]=por.closed(-5.5,-5)
A[7][5]=por.closed(-4.5,-4)
B=np.zeros((8,1),dtype=object)
B[0]=por.closed(1,2)
B[1]=por.closed(2,3)
B[2]=por.closed(2,3.5)
B[3]=por.closed(2.25,4)
B[4]=por.closed(2,3.5)
B[5]=por.closed(1.25,2)
B[6]=por.closed(1.5,2)
B[7]=por.closed(2,2.25)
A_t=np.transpose(A)


def matrix_multiplication(E, R):
    '''matrix multiplication'''
    # dimensions of A and B
    n1 = E.shape[0]
    m1 = R.shape[1]

    # initialize the result matrix
    C = np.empty((n1,m1),dtype=object)
    for e in range(n1):
        for r in range(m1):
            C[e][r]=por.closed(0,0)

    # perform matrix multiplication
    for i in range(n1):
        for j in range(m1):
            for k in range(E.shape[1]):
                #print(K.multiplication(E[i][k],R[k][j]))
                C[i][j]=K.addition(C[i][j],K.multiplication(E[i][k],R[k][j]))
    return C
A_times_at=matrix_multiplication(A_t,A)

def matrix_inverse(matrix):
    """Calculates the inverse of a matrix using LU decomposition."""
    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    # Create the LU decomposition of the matrix
    n = len(matrix)
    L = np.empty((n, n),dtype=object)
    U = np.empty((n, n),dtype=object)
    for i in range(n):
        for j in range(n):
            L[i][j]=por.closed(0,0)
            U[i][j]=por.closed(0,0)

    # Fill in the diagonal elements of U with 1
    for i in range(n):
        U[i][i] = por.closed(1,1)
        L[i][i]= por.closed(1,1)
    ## Fill in the other elements of U with 0
    s = np.empty((n, n),dtype=object)
    for ele_1 in range(n):
        for ele_2 in range(n):
            s[ele_1][ele_2]=por.closed(0,0)
    # Perform LU decomposition using Gaussian elimination
    for j in range(n):
        for i in range(j+1):
            for k in range(i):
                s[i][j] = K.addition(s[i][j],K.multiplication(L[i][k] ,U[k][j]))
                L[i][j] = K.division(K.subtraction(matrix[i][j] , s[i][j]),U[j][j])
        for i in range(j, n):
            for k in range(j):
                s[i][j] = K.addition(s[i][j],K.multiplication(L[j][k] , U[k][i]))
                U[j][i] = K.subtraction(matrix[j][i] , s[i][j])
            # Calculate the inverse of the matrix

    inverse_matrix = np.empty((n, n),dtype=object)
    for ele_1 in range(n):
        for ele_2 in range(n):
            inverse_matrix[ele_1][ele_2]=por.closed(0,0)
    #y=np.zeros((1,n),dtype=object)

    for j in range(n):
        # Solve Ly = e_j for y using forward substitution
        y = [0] * n
        for z in range(n):
            y[z]=por.closed(0,0)
        y[j] = por.closed(1,1)

        for i in range(n):
            for k in range(i):
                s[i][j] = K.addition(s[i][j],K.multiplication(L[i][k] , y[k]))
                y[i] = K.division(K.subtraction(y[i] , s[i][j]), L[i][i])


        # Solve Ux = y for x using backward substitution
        x = [0] * n
        #print(x)
        for z in range(n):
            x[z]=por.closed(0,0)

        for i in reversed(range(n)):
            for k in range(i+1, n):
                s[i][j] = K.addition(s[i][j],K.multiplication(U[i][k] , x[k]) )
                x[i] = K.division(K.subtraction(y[i] , s[i][j]),U[i][i])
        #print(x)
        inverse_matrix[j] = x

    return inverse_matrix
Inv=matrix_inverse(A_times_at)



Inv_A_A_T_X_A_T= matrix_multiplication(Inv,A_times_at)
X=matrix_multiplication(Inv_A_A_T_X_A_T,B)

print("The Intervals of co efficients are:",X)

ca1.horizontal_line()
stop_time=t.time()
ca1=h.Footer((stop_time-Start_time))
ca1.run_time()

