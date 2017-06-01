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
a=Restaurant("you","me")
a.describe_restaurant()
a.open_restaurant()