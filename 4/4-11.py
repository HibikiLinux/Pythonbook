#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('kkk')
print("My favorite pizzas are:")
for i in my_foods:
    print(i)
print("Myfriend's favorite pizzas are:")
for i in friend_foods:
    print(i)