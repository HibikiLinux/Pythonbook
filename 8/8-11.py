#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen

def  make_great(names):
    namess = []
    for i in names:
        namess.append("the great "+i)
    return namess
name=["wang","zhou","li"]
ss=["sss","fff","ttt"]
tt=["wew","www","bb"]
a=make_great(name)
b=make_great(ss)
c=make_great(tt)
print(a)
print(b)
print(c)
print(name)