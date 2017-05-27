#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
pop_motorcycles=motorcycles.pop()
print(pop_motorcycles)
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
motorcycles.remove('yamaha')
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki','yamaha']
motorcycles.remove('yamaha')
print(motorcycles)
