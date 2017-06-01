#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def make_album(name,zhuanji,number=33):
    z={"name":name,"zhuanji":zhuanji,"number":number}
    return z

while True:
    p=input("名字")
    if p=="q":
        break
    pp=input("专辑")
    if pp=="q":
        break
    else:
        #zhuan = make_album("zhou", "666", number=44)
        zhuan = make_album(p,pp)
        print(zhuan)