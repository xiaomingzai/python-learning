#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
#print('{0}的成绩提升了{1:.2f}%' % r)
#      '{0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
print('{0}的成绩提升了 {1:.2f}%'.format('小明',r))


#       'Hi, %s, you have $%d.' % ('Michael', 1000000)
print ('%s的成绩提升了 %.2f%%'%('小明',r))
#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
