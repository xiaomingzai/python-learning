#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##list 
names=['Michael','Bob','Tracy']
score=[95,75,85]


##dict
d={'Michael':95,'Bob':75,'Tracy':85}
print(d)
print(d['Michael'])
d['Michael']=96
print(d['Michael'])
print('Michael' in d)
print(d.get('Michael'))

d['Lucy']=100
print(d.get('Lucy'))
print(d)
d.pop('Lucy')
print(d)
