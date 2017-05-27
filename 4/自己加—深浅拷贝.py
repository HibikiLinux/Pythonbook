#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import copy
def p():
    print(a)
    print(b)
    print(c)
    print(d)
    print("......")
a=['aa','bb',['cc',77]]
b=a[:]
c=a.copy()
d=copy.deepcopy(a)
p()
a[1]=333
a[2][1]=666
p()