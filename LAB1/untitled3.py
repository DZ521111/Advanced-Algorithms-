# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:43:34 2020

@author: DHRUV
"""
import random
count = 0

def partition(input_list, low, high):
    global count
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        count += 1
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] =  input_list[j], input_list[i]
    input_list[i+1], input_list[high] = input_list[high], input_list[i+1]
    return (i+1)

def quickSort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list,low,high)
        quickSort(input_list, low, partition_index - 1)
        quickSort(input_list, partition_index + 1, high)
        
input_l = []
for i in range(0, 2000):
    input_l.append(random.randint(1, 500))
list_length = len(input_l)
quickSort(input_l, 0, list_length -1)
print(count)