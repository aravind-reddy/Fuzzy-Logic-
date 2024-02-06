#header
"""module used for time"""
import time as t
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

num=[0,1]
N=9
for i in range(2,N):
    num.append(num[i-2]+num[i-1])
for i in range(9):
    print("Sequence" ,i+1,"is", num[i])

# footer


ca1.horizontal_line()
stop_time=t.time()
ca1=h.Footer((stop_time-Start_time))
ca1.run_time()
