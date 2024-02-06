#header
"""module used for time"""
import time as t
import numpy as np
import matplotlib.pyplot as plt
import portion as por
import skfuzzy as fuzzy
import ece6397_pasunuri_helper_headerfooter as h
ca1=h.Header("Aravind Reddy","Pasunuri","Assignment 6","Fuzzy Membership Functions")
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
u=h.Port()
a_int=por.closed(1,12)
b_int=por.closed(2,5)
x=np.arange(1,13,1)
k_add=u.addition(a_int,b_int)
k_sub=u.subtraction(a_int,b_int)
k_mul=u.multiplication(a_int,b_int)
y_add=np.arange(k_add.lower,k_add.upper+1,1)
y_sub=np.arange(k_sub.lower,k_sub.upper)
y_mul=np.arange(k_mul.lower,k_mul.upper,1)
A_I=4
B_I=6
C_I=11
P_I=3
Q_I=4
R_I=5
a_fuz= fuzzy.trimf(x, [A_I,B_I,C_I])
print("Membership function 1:",a_fuz)
b_fuz= fuzzy.trimf(x, [P_I,Q_I,R_I])
print("Membership function 2:",b_fuz)
c_fuz= fuzzy.trimf(y_add, [(A_I+P_I),(B_I+Q_I),(C_I+R_I)])
print("Addition operation:",c_fuz)
d_fuz= fuzzy.trimf(y_sub, [(A_I-R_I),(B_I-Q_I),(C_I-P_I)])
print("Subtraction Operation:",d_fuz)
e_fuz=fuzzy.trimf(y_mul,[(A_I*P_I),(B_I*Q_I),(C_I*R_I)])
print("Multiplication Operation",e_fuz)
#generating graphs
fig1, (ax_one,ax_two,ax_opr)=plt.subplots(nrows=3, ncols=1)
ax_one.plot(x,a_fuz)
ax_one.set_title('1st Membership function')
ax_two.plot(x,b_fuz)
ax_two.set_title('2nd Membership fucntion')
ax_opr.plot(y_add,c_fuz)
ax_opr.set_title('Addition Operation')
fig1.suptitle('Addition Operation')
fig1.tight_layout()


fig2, (ax_one,ax_two,ax_opr)=plt.subplots(nrows=3, ncols=1)
ax_one.plot(x,a_fuz)
ax_one.set_title('1st Membership function')
ax_two.plot(x,b_fuz)
ax_two.set_title('2nd Membership fucntion')
ax_opr.plot(y_sub,d_fuz)
ax_opr.set_title('subtraction Operation')
fig2.suptitle('Subtraction Operation')
fig2.tight_layout()


fig3, (ax_one,ax_two,ax_opr)=plt.subplots(nrows=3, ncols=1)
ax_one.plot(x,a_fuz)
ax_one.set_title('1st Membership function')
ax_two.plot(x,b_fuz)
ax_two.set_title('2nd Membership fucntion')
ax_opr.plot(y_mul,e_fuz)
ax_opr.set_title('Multiplication Operation')
fig3.suptitle('Multiplication Operation')
fig3.tight_layout()
ca1.horizontal_line()
stop_time=t.time()
ca1=h.Footer((stop_time-Start_time))
ca1.run_time()
plt.show()
