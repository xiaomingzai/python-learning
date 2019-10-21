#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age=int (input("please input  your age : "))
if age >= 18:
	print('your age is',age)
	print('you are an adult')
elif age>=6:
	print('your age is',age)
	print('you are a teenager')
else:
	print('your age is',age)
	print('you are a kid')