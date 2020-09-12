# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:32:26 2020

@author: DHRUV
"""

def BoyerMooreHorspool(pattern, string):
    pattern_l = len(pattern)
    skepText_l = len(string)
    if pattern_l > skepText_l:
        return -1
    skip = []
    for i in range(256):
        skip.append(pattern_l)
    for i in range(pattern_l - 1): 
        skip[ord(pattern[i])] = pattern_l - i - 1
    skip = tuple(skip)
    i = pattern_l - 1
    while i < skepText_l:
        j = pattern_l - 1
        k = i
        while j >= 0 and string[k] == pattern[j]:
            j -= 1
            k -= 1
        if j == -1:
            return k + 1
        i += skip[ord(string[i])]
    return -1

if __name__ == '__main__':
    string = input("Enter the string : ")
    pattern = input("Enter the pattern : ")
    pos = BoyerMooreHorspool(pattern, string)
    if pos > -1:
        print (pos)
    else:
        print ("Not Found")
