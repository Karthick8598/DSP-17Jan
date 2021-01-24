# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:50:52 2021

@author: vikas
"""


def max_ele(ls):
    m = 0
    for n in ls:
        if (n > m):
            m = n
    return (m)


l1 = list(range(1, 100000000))
max_ele(l1)


import numpy as np
np.max(l1)
