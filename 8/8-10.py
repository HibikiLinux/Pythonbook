#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def  make_great(names):
    n=0
    for i in names:
        names[n]="the great "+i
        n=n+1
name=["wang","zhou","li"]
make_great(name)
print(name)