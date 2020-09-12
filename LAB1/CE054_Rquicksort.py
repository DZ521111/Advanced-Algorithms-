# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:35:12 2020

@author: DHRUV
"""


from random import randint
comparision = 0

def quicksort(arr, start, end):
    if (start < end):
        pivot_index = partition(arr, start, end)
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)
    return arr

def partition(arr, start, end):
    global comparision
    pivot = randint(start, end)
    temp1 = arr[end]
    arr[end], arr[pivot] = arr[pivot], temp1
    pivot_index = start
    for i in range(start, end):
        comparision += 1
        if (arr[i] <= arr[end]):
            temp1 = arr[i]
            arr[i], arr[pivot_index] = arr[pivot_index], temp1
            pivot_index += 1
    temp2 = arr[end]
    arr[end], arr[pivot_index] = arr[pivot_index], temp2
    return pivot_index

if __name__ == "__main__":
    arr = []
    for i in range(2500):
        arr.append(i)
    print(quicksort(arr, 0, len(arr) - 1))
    print(comparision)
    