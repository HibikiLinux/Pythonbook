#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def make_car(a,b,**kwargs):
    car={}
    car["品牌"]=a
    car["型号"]=b
    for key,value in kwargs.items():
        car[key]=value
    return car
ca = make_car('subaru', 'outback', color='blue', tow_package=True)
print(ca)


