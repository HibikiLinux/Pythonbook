#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
age=input("输入年龄")
age=int(age)
if age<2:
    print("他是婴儿")
elif 2<= age < 4:
    print("蹒跚学步")
elif 4<= age < 13:
    print("他是儿童")
elif 13<= age < 20:
    print("他是青少年")
elif 20<= age <65:
    print("他是成年人")
else:
    print("他是老年人")
