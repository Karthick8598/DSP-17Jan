# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:00:46 2021

@author: vikas
"""

#numpy

import numpy as np

np.random.randint(10)

np.random.randint(10, 20)

x1 = np.random.randint(100, 200, size=10)
x1
x1.shape

x2 = np.random.randint(100,200, size = (3,4))
x2
x2.shape

x3 = np.random.randint(100, 200, size = (2,3,4))
x3

x1[0]=20
x1[2:-2]


x2
x2[1][1]
x2[1][2]
x2[1,2]
x2[0,:]

x2[0:2,:]
x2
x2[:2,:]
x2[0,2:]

x2[:,2:]

x2[-1,-2:]


x2[2, 2:4]


x4  = np.random.randint(100, 200, size = (6,6))
x4

x4[::2,]

x4[:,::2]

x4
x4[::2,::2]


import numpy as np

n1 = np.arange(20)
n1

n2 = np.arange(10,20)
n2

n3 = np.arange(10, 20, 2)
n3


n4 = np.arange(10, 22)

n4.shape

n4.reshape(3,4)

n4.reshape(4,3)

n4.reshape(2,6)

n4.reshape(6,2)

n4.reshape(4,4)


n5 = np.random.randint(10,22, size=(3,4))
n5

n6 = np.zeros((3,4), dtype= int)
n6

n7 = n5+n6

n7


n8 = np.ones((3,4))

n8

n9 = n5 * n8

n9

n10 = n7*n9
n10


np.eye(3,3)

ls1 = np.linspace(0,10, num = 5)

ls1


import math

math.sin(90)

math.cos(90)

sum(ls1)
max(ls1)
min(ls1)

np.mean(ls1)
np.std(ls1)
np.var(ls1)

a = -10.4

math.ceil(a)
math.floor(a)
math.log(10)
math.log10(10)
math.factorial(5)
math.gcd(10, 5)
math.pi
math.pow(10, 5)


import matplotlib.pyplot as plt

n1 = np.random.normal(50, 10, size = 10)
n1
plt.hist(n1)


n1
np.mean(n1)
np.std(n1)


np.floor([1.2, 1.6])
np.ceil([1.2, 1.6])
np.trunc([1.2, 1.6])
np.round([1.2, 1.6])


np.trunc([-1.2, -1.6])
np.floor([-1.2, -1.6])
np.round([-1.2, -1.6])

np.round([1.23434, 1.654455],2)




x4=np.array([1,2,3,4,5,6,7])

x5=np.array([11,12,13,14,15,16,17])

np.concatenate([x4, x5])


x6 = np.random.randint(100,200, size=(3,4))

x7 = np.random.randint(200,300, size=(3,4))

x6
x7

np.concatenate([x6,x7], axis=0)

np.concatenate([x6,x7], axis=1)


np.add(x6,x7)
np.multiply(x6,x7)



x8 = np.random.randint(100,200, size=(500,10))

x8.shape

x8

np.all(x8>190)

np.all(x8>99)

np.any(x8>190)

np.any(x8>200)


x9 = np.random.randint(100,200, size=(5,6))
x9
x9>150

np.any(x9>150)

np.sum(x9>150)

np.sort(x9, axis= 0)











































































































