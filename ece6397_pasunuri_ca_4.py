#header
"""module for portion"""
import time as t
import portion as por
import ece6397_pasunuri_helper_headerfooter as h
ca1=h.Header("Aravind Reddy","Pasunuri","Assignment 1","Fibonacci Series")
for i in range(2):
    ca1.horizontal_line()
ca1.student_name()
ca1.ca_name()
ca1.horizontal_line()
ca1.description()
Start_time=t.time()
print("START RUN")
ca1.horizontal_line()

#body
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
    

    
A= por.closed(2,14)
print("A=",A)
B=por.closed(1,16)
print("B=",B)
p=Port()
print("A+B : [A_l + B_l , A_u + B_u] : ",p.addition(A,B))
print("A-B : [A_l - B_u , A_u - B_l] : ",p.subtraction(A,B))
#print("1/A: ",reciprocal(A))
print("A*B:[min(P),max(P)] where P={A_l*B_l,A_u*B_u,A_l*B_u,A_u*B_l}:",p.multiplication(A,B))
print("A/B : A*B^-1 : ",p.division(A,B))
print("max(A,B) : [maximum[A_l,B_l] , maximum[A_u,B_u]] : ",p.maxnmin(A,B))
print("min(A,B) : [minimum[A_l,B_l] , minimum[A_u,B_u]] : ",p.minimum(A,B))

# footer
ca1.horizontal_line()
stop_time=t.time()
ca1=h.Footer((stop_time-Start_time))
ca1.run_time()
