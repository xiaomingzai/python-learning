#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#求x的n次方
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print('2的4次方等于：',power(2,4))
print('2的平方等于：',power(2))



'''
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)
'''
#把年龄和城市设为默认参数
def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
print(enroll('Sarah', 'F',7,city='Tianjin'))



#可变参数
def calc(*numbers):
	sum=0
	for  n in numbers:
		sum=sum+n*n
	return sum
print(calc(1,2))

#关键字参数
def persion(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

print(persion('Micheal',30))
print(persion('Bob',35,city='Beijing'))

extra={'city':'Beijing','job':'Engineer'}
print(persion('Jack',24,city=extra['city'],job=extra['job']))
print(persion('Jack',24,**extra))

#命名关键字参数
def persion1(name,age,*,city,job):   #只接收city和job作为关键字参数
	print(name,age,city,job)
print(persion1('Jack',34,city="Beijing",job='Engineer'))


#作业
#接收一个或多个数并计算乘积
def product(*args):
	sum=1
	for n in args:
		sum=sum*n
	return sum
print('2=',product(2))	
print('2*3*4=',product(2,3,4))
print('2*3*4*5=',product(2,3,4,5))
