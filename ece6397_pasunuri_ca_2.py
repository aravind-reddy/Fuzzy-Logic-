#header
"""module used for time"""
import time as t
import ece6397_pasunuri_helper_headerfooter as h
ca1=h.Header("Aravind Reddy","Pasunuri","Assignment 2","Distributive Laws")
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
A=set(range(2,11,2))
B=set(range(1,6))
C=set(range(5,11))
S=set(range(1,11))
E=set()
class DistributiveLaws:
    "for union and intersection"
    def __init__(self,s_i):
        """init"""
        self.s_i=s_i
    def cup(self,a_u,b_u):
        "for union"
        return a_u.union(b_u)
    def cap(self,a_i,b_i):
        "for intersection"
        return a_i.intersection(b_i)
    def compliment(self,a_b):
        "compliment"
        return (self.s_i).difference(a_b)

d_l=DistributiveLaws(S)
print("Distributive law-1")
print("A cap (B cup C): ",(d_l.cap(A,d_l.cup(B,C))))
print("(A cap B) cup (A cap C): ",d_l.cup(d_l.cap(A,B),d_l.cap(A,C)))
print("Distributive law-2")
print("A cup (B cap C): ",(d_l.cup(A,d_l.cap(B,C))))
print("(A cup B) cap (A cup C): ",d_l.cap(d_l.cup(A,B),d_l.cup(A,C)))
print("Distributive law-3")
print("(A cup A): ",d_l.cup(A,A))
print('A: ',A)
print("Distributive law-4")
print("(A cap A): ",d_l.cap(A,A))
print("A: ",A)
print("Distributive law-5")
print("A cup (A cap B): ",d_l.cup(A,d_l.cap(A,B)))
print("A: ",A)
print("Distributive law-6")
print("A cap (A cup B): ",d_l.cap(A,d_l.cup(A,B)))
print("A: ",A)
print("Distributive law-7")
print("A cup (Ā cap B): ",d_l.cup(A,d_l.cap(d_l.compliment(A),B)))
print("(A cup B): ",d_l.cup(A,B))
print("Distributive law-8")
print("A cap (Ā cup B): ",d_l.cap(A,d_l.cup(d_l.compliment(A),B)))
print("(A cap B): ",d_l.cap(A,B))
print("Distributive law-9")
print("A cup S: ",d_l.cup(A,S))
print("S: ",S)
print("Distributive law-10")
print("A cap E: ",d_l.cap(A,E))
print("E: ",E)
print("Distributive law-11")
print("A cup E: ",d_l.cup(A,E))
print("A: ",A)
print("Distributive law-12")
print("A cap S: ", d_l.cap(A,S))
print("A: ",A)
print("Distributive law-13")
print("A cap Ā: ",d_l.cap(A,d_l.compliment(A)))
print("E: ",E)
print("Distributive law-14")
print("A cup Ā: ",d_l.cup(A,d_l.compliment(A)))
print("S: ",S)

# footer
ca1.horizontal_line()
stop_time=t.time()
ca1=h.Footer((stop_time-Start_time))
ca1.run_time()
