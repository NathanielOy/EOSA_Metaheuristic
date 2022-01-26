# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:59:14 2021

@author: Oyelade
"""

import numpy as np
#(xa_high > 2000).any()
#(a-b).any() or (a-b).all().
def cmp_to_key(mycmp, index):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj, index) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def ucompare(x, y, index):
    if type(x) != tuple and type(y) != tuple:
        return ucompare_default(x, y, index)
    x1, x2=x
    y1, y2=y 
    #if isinstance(x2, float) and isinstance(y2, float): #ucompare_default(x, y, index)        
    s=x2[index] < y2[index]
    #print(str(x2[index])+'------'+str(s)+'------'+str(y2[index]))
    return s

def ureverse(x, y, index):
    if type(x) != tuple:
        return ucompare_default(x, y, index)
    x1, x2=x
    y1, y2=y
    return (y2[index] < x1[index]).all()

def ucompare_default(x, y, index):
    return x[index] < y[index] #).all()

def ureverse_default(x, y, index):
    return (y[index] < x[index]).all()