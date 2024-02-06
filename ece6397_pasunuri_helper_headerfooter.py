"for header and footer"

import portion as por
class Header:
    "for header"
    def __init__(self,lname,fname,caname,des):
        "init"
        self.lname=lname
        self.fname=fname
        self.caname=caname
        self.des=des

    def horizontal_line(self):
        "for horizontal line"
        print('-'*79,end='')
        print()
    def student_name(self):
        "for student name"
        print("Last Name:"+ self.lname)
        print("First Name:"+ self.fname) 
    def ca_name(self):
        "for computer assignment"
        print("Computer Assignment:"+ self.caname.upper())
    def description(self):
        "for description"
        print("Description:" + self.des)

class Footer:
    "footer"
    def __init__(self,sttime):
        "init"
        self.sttime=sttime
    def run_time(self):
        "run time"
        print("run time:",round(self.sttime,6)*10,"s")
        print("END RUN")
    def run_time1(self):
        "for printing run1"
        print("run1")

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