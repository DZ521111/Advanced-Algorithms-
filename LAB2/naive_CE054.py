# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:43:05 2020

@author: DHRUV
"""

def search (pattern, string):
    len_pattern, len_string = len(pattern), len(string)
    for ele in range(len_string - len_pattern + 1):
        i = 0
        while (i < len_pattern):
            if (string[ele + i] != pattern[i]):
                break
            i += 1
        if (i == len_pattern):
            return ele
    else:
        return -1

if __name__ == "__main__":
    string = input("Enter the text : ")
    pattern = input("Enter the pattern : ")
    index_ = search(pattern, string)
    if (index_ != -1):    
        print(f"pattern found at index {index_}")                
    else:
        print("pattern not found")