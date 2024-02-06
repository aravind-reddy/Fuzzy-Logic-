#header
"""module used for time"""
import time as t
import ece6397_pasunuri_helper_headerfooter as h
ca1=h.Header("Aravind Reddy","Pasunuri","Assignment 3","Power Set")
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

class Powerset:
    "class for calculating power set"
    def __init__(self,filename):
        self.filename=filename
    def process(self):
        "fucntion for power set"
        with open(self.filename,'r',encoding='utf-8') as file_name:
            lines=file_name.readlines()
            lines[0]=set()
            for j in range(1, len(lines)):
                lines[0].add(lines[j].rstrip())
            list_powerset = [set()]
            for elem in (lines[0]):
                for sub_set in list_powerset:
                    list_powerset = list_powerset + [sub_set.union(set([elem]))]
            print("number of elements in power set:",len(list_powerset))
        return list_powerset
    def print_set(self,list_set):
        '''function printing power set elements'''
        for x_1 in list_set:
            print(x_1)

power_set=Powerset(input())
y_1=power_set.process()
power_set.print_set(y_1)
# footer
ca1.horizontal_line()
stop_time=t.time()
ca1=h.Footer((stop_time-Start_time))
ca1.run_time()
