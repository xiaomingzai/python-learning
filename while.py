#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#计算100以内所有奇数之和
sum=0
n=99

while n>0:
	sum=sum+n
	n=n-2
print(sum)

#打印出1~100
m=1
while m<=100:
	print(m)
	m=m+1
print ('END')

#如果要提前结束循环，可以用break语句
a=1
while a<=100:
	if a>10:   # 当n = 11时，条件满足，执行break语句
		break  # break语句会结束当前循环
	print(a)
	a=a+1
print ('END')

#在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
#只打印1~10之间的奇数
b=0
while b<10:
	b=b+1
	if b%2==0:    # 如果b是偶数，执行continue语句
		continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	print(b)