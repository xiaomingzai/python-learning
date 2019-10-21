#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names=['Michael','Bob','Lucy']
for name in names:
	print(name)

#range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
print('range(5)=',list(range(5)))

sum=0
for x in range(101):
	sum=sum+x
print(sum)