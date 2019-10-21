#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##abs求绝对值
print('abs(-20)=',abs(20))

print('max(1,2,30)=',max(1,2,30))


##类型转换
print('int(\'123\')=',int('123'))
print('int(12.34)=',int(12.34))
print('float(12.34)=',float(12.34))
print('str(1.23)=',str(1.23))
print('bool(1)=',bool(1))
print('bool(\'\')=',bool(''))

##hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
print('hex(255)=',hex(255))


def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x
print('my_abs(99)=',my_abs(-99))



#从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标
import math
def move(x,y,step,angle=0):##参数angle的默认值设定为0
##def move(x,y,step,angle):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny
x,y=move(100,100,60,math.pi/6)
print('x,y=',x,y)



#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。
#def quadratic(a, b, c):
#	a=float(input('请输入a:'))
#	b=float(input('请输入b:'))
#	c=float(input('请输入c:'))

aa=float(input('请输入a:'))
bb=float(input('请输入b:'))
cc=float(input('请输入c:'))
def quadratic(a,b,c):
	if a==0 or (b**2-4*a*c)<0:
		print('无解')
	else:
		x1=(-b+math.sqrt(b**2-4*a*c))/2*a
		x2=(-b-math.sqrt(b**2-4*a*c))/2*a
		print('方程式的解x1=%.2f,X2=%.2f'%(x1,x2))
		return x1,x2
quadratic(aa,bb,cc)
