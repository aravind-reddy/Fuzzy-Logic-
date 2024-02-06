#header
"""module used for time"""
import time as t
import sys
import numpy as np
import ece6397_pasunuri_helper_headerfooter as h
ca1=h.Header("Aravind Reddy","Pasunuri","Assignment 7","Fuzzy Implications")
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
# Get the arguments
ARG_1 = sys.argv[1]
ARG_2 = sys.argv[2]
ARG_3 = sys.argv[3]
list_arg3= ARG_3.split()

# Create the list of numbers
truth_logic1 = np.around(np.linspace(0,1,int(ARG_1)),decimals=2)
truth_logic2 = np.around(np.linspace(0,1,int(ARG_2)),decimals=2)

# Display the list
class Fuzzy:
    "Class for Fuzzy Implications"
    def __init__(self):
        pass
    def a_truth(self, arga_1, arga_2):
        "for a"
        implicationa = min(arga_1,arga_2)
        return implicationa
    def b_truth(self, argb_1, argb_2):
        "for b"
        implicationb= argb_1*argb_2
        return implicationb
    def c_truth(self,argc_1,argc_2):
        "for c"
        implicationc= min(1,(1+argc_2-argc_1))
        return implicationc
    def d_truth(self, argd_1,argd_2):
        "for d"
        implicationd=max(min(argd_1,argd_2),(1-argd_1))
        return implicationd
    def e_truth(self, arge_1,arge_2):
        "for e"
        implicatione= max((1-arge_1),arge_2)
        return implicatione
    def f_truth(self, argf_1,argf_2):
        " for f"
        if argf_1<=argf_2:
            implicationf=max(1,0)
            return implicationf
        implicationf=argf_2/argf_1
        return implicationf

sc=Fuzzy()
for k in truth_logic1:
    for l in truth_logic2:
        for method in list_arg3:
            if method=='a':
                print( f' {k} =>  {l}  = {sc.a_truth(k,l):.2f}, a')
            elif method=='b':
                print( f' {k} =>  {l}  = {sc.b_truth(k,l):.2f}, b')
            elif method=='c':
                print( f' {k} =>  {l}  = {sc.c_truth(k,l):.2f}, c')
            elif method=='d':
                print( f' {k} =>  {l}  = {sc.d_truth(k,l):.2f}, d')
            elif method=='e':
                print( f' {k} =>  {l}  = {sc.e_truth(k,l):.2f}, e')
            elif method=='f':
                print( f' {k} =>  {l}  = {sc.f_truth(k,l):.2f}, f')
        print()
        print()



ca1.horizontal_line()
stop_time=t.time()
ca1=h.Footer((stop_time-Start_time))
ca1.run_time()
