#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def  make_great(names):
    for i in range(len(names)):
        names[i]=names[i]+"the great"
name=["wang","zhou","li"]
make_great(name)
print(name)