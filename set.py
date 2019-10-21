#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##list 
names=['Michael','Bob','Tracy']
score=[95,75,85]


##set
##要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print('s=',s)

s.add(4)    ##在set中，没有重复的key
print('s=',s)

s.remove(4)
print('s=',s)

s2 = set([2, 3, 4])
print('s & s2 =',s & s2)
print('s | s2 =',s | s2)
