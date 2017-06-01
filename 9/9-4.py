#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("正在营业")
    def number_served(self,number=0):
        self.number=number
a=Restaurant("bb","yy")
b=a.number_served()
print(a.number)
c=a.number_served(7)
print(a.number)
