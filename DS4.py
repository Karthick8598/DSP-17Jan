# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:53:04 2021

@author: vikas
"""

a =10
b=20

a = b

a == b
a < b
a > b
a<=b
a>=b
a!=b


if (a > b):
    print("yes")


if (a > b):
    print ("yes")
else:
    print ('No')
    


m = int(input("Enter Marks -> "))

if (m>80):
    print ("A")

elif(m>70 and m <= 80):
    print("B")
    
elif(m>60 and m <= 70):
    print("C")

elif(m>50 and m <= 60):
    print("D")

else:
    print("Fail")





x=3; y=4; z=5

if x < y and y < z:
  print("Both conditions are True")


z=2

if x < y or y > z:
  print("Both conditions are True")



if (x < y) or (y > z) :
  print("Either conditions are True")



if ((x < y) or (y > z)) and (x > 10):
    print("Both conditions are True")
else:
    print("Conditions are not True")




if ((x < y) or (y > z)) or (x > 10):
    print("Either conditions are True")
else:
    print("Conditions are not True")

(x < y) or (y > z) and (x > 10)
x<y, x>z, x<10
True or False and True  #left to right

(x > 10) and (x < y) and (y > z)  

if (x < y) or (y > z) and (x > 10):
    print("Either conditions are True")
else:
    print("Conditions are not True")













