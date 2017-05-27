#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(sorted(cars))
# print(cars)
# cars.reverse()
# print(cars)
# print(len(cars))
#32P的3-8练习
jingdian=['shenzhen','taiwan','mosike','xizang','dongjing']
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始 Python 列表。
print(jingdian)
# 使用 sorted() 按字母顺序打印这个列表，同时不要修改它。
print(sorted(jingdian))
# 再次打印该列表，核实排列顺序未变。
print(jingdian)
# 使用 sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print((sorted(jingdian)))
# 再次打印该列表，核实排列顺序未变。
print(jingdian)
# 使用 sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
jingdian.sort()
print(jingdian)
# 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
jingdian.sort(reverse=True)
print(jingdian)
