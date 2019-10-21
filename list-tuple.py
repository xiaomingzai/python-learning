#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list
classmates=['Michael','Bob','Lucy']
print('classmates=',classmates)
print(len(classmates))
print('classmates[0]=',classmates[0])
print('classmates[-1]=',classmates[-1])  #倒数第一个，等价于print(classmates[2])
print('classmates[-2]=',classmates[-2])  #倒数第二个

#往list中追加元素到末尾
classmates.append('Adam')
print('classmates=',classmates)

#把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'jack')
print('classmates=',classmates)

#删除list末尾的元素，用pop()方法
classmates.pop()
print('classmates=',classmates)

#删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print('classmates=',classmates)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1]='Jack'
print('classmates=',classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print("s=",s)
print(s[2][1])


#tuple 
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates1=('Michael','Bob','Lucy')
print('classmates1=',classmates1)
#当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

#定义只有一个元素的tuple时候，必须写成下面的格式，否则默认为进行()的运算。

tuplee = (1,)
#tuple指的是指向的数据不变，也就是说tuple中含有list的时候