#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
f = open("yesterday.txt",encoding="utf-8")
count=0
for line in f:
    if count==9:
        print('--------------')
        count += 1
        continue
    print(line)
    count+=1