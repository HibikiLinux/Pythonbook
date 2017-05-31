#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
current_users=["admin", "lv", "wang", "zhuang", "liu"]
new_users=["admin","lv","alex"]
for i in new_users:
    if i in current_users:
        print(i+"这个用户名被使用请使用别名")
    else:
        print(i+"这个用户名未被使用")



