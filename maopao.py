#!/usr/bin/env python3
# -*- coding: utf-8 -*-
arr = [64,34,25,12,22,11,90]
n = len(arr)
print('排序前：',arr)

# 遍历所有数组元素
#比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好
for i in range(n-1):    #range(n)=[0,1,...,n-1]
	for j in range(0, n-i-1):
		if arr[j] > arr[j+1] :
			arr[j], arr[j+1] = arr[j+1], arr[j]
print('排序后：',arr)


#可选升降序的冒泡排序, order>0升序，order<0降序
'''
def bubbleSort(arr,order):
    max = len(arr)
    for i in range(0, max):
        j = 1
        while(j<max-i):
            if((arr[j-1]>arr[j]) and (int(order)>0)) or ((arr[j-1]<arr[j]) and (int(order)<0)):
                arr[j-1], arr[j] = arr[j], arr[j - 1]
            j += 1
        i += 1
    return arr


A = [64, 25, 12, 22, 11] 
print(bubbleSort(A, -1))
print(bubbleSort(A, 1))
'''