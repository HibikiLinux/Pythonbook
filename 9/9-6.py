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
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    def pt_flavors(self):
        print(self.flavors)
        for i in self.flavors:
            print(i)

bbb=IceCreamStand("冰激凌小店","冰激凌","草莓","香草","蓝莓")
bbb.pt_flavors()
