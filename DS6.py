# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:00:33 2021

@author: vikas
"""

a=10
b=20

print (a+b)
print (a-b)
print (a*b)
print (a/b)


#User Defined Functions

def oper():
    a=20
    b=30
    print (a+b)
    print (a-b)
    print (a*b)
    print (a/b)

oper()

oper()

oper()


def oper1(a,b):
    print (a+b)
    print (a-b)
    print (a*b)
    print (a/b)


oper1(5, 7)

oper1(8,3)



def cleanstr(name):
    name = name.strip()
    name = name.lower()
    name = name.center(20)
    return(name)

cname = cleanstr("  ViKAs      ")

print(cname)




cname = cleanstr("  KhuLLAR")

print(cname)



l1 = [1,2,4,5]

lengthofL1 = len(l1)

lengthofL1




def mat(a,b):
    c= a+b
    d= a-b
    return(c,d)


a1 , b1 = mat(10,20)

a1
b1



def emp(ecode, name, email='None'):
    print (ecode, name, email)


emp('111', 'aaa', 'a@a.com')

emp('111', 'aaa')



"""The function max() from exercise 1) and the function 
max_of_three() from exercise 2) will only work for two 
and three numbers, respectively. But suppose we have a 
much larger number of numbers, or suppose we cannot tell 
in advance how many they are? Write a function max_in_list() 
that takes a list of numbers and returns the largest one."""

l1 =[2,3,4,51,9]

max(l1)



def max_ele(ls):
    m = 0
    for n in ls:
        if (n > m):
            m = n
    return (m)



max_ele(l1)




















































