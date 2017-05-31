#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
bjinfo={"country":"中国","population":300,"fact":"G"}
shinfo={"country":"中国","population":200,"fact":"G"}
gzinfo={"country":"中国","population":100,"fact":"G"}
cities={"beijing":bjinfo,"shanghai":shinfo,"guangzou":gzinfo}
print(cities["shanghai"]["population"])
