#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
sandwich_orders=["egg","pastrami","chicken","pastrami","sausage","pastrami"]
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)
