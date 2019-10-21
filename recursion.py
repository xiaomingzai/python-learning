#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##递归
##如果一个函数在内部调用自身本身，这个函数就是递归函数
##尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式

#fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
'''

def fact(n):
	return fact_iter(n,1)
#把每一步的乘积传入到递归函数中
def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)
	
	
#从下面开始按大小顺序重新摆放在另一根柱子上。
#并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘
#汉诺塔的移动可以用递归函数非常简单地实现
def hanoi(n,a,b,c):
	if n==1:
		print(a,'-->',c)
	else:
		hanoi(n-1,a,c,b)# 借助C柱，将n-1个圆盘从A柱移动到B柱
		print(a,'-->',c)# 将A柱最底层的圆盘移动到C柱
		hanoi(n-1,b,a,c)# 借助A柱，将n-1个圆盘从B柱移动到C柱
print(hanoi(5,'A','B','C'))