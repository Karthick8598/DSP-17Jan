# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:30:07 2021

@author: vikas
"""

import random as rd

r1 = rd.randint (1,10)
r1

l1 = [111,222,333,444,555]

rd.choice(l1)

rd.choices(l1, k=10)


Gender = ['M','F']

gen = rd.choices(Gender, k=10)

rno = range(1,11)

z1 = zip(rno,gen)

list(z1)
