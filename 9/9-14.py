#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
# from random import randint
# x = randint(1, 6)
# print(x)
from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        self.n=randint(1,self.sides)
        print(self.n)
g6=Die(10)
g6.roll_die()
