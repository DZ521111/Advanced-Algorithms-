# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:17:17 2020

@author: DHRUV B KAKADIYA
"""

total_char = 256

def search(pat, txt, modulo):
    len_pattern = len(pat)
    len_string = len(txt)
    flag, j, value, temp, hash_ = 0, 0, 0, 0, 1
    for i in range(len_pattern - 1):
        hash_ = (hash_ * total_char) % modulo
    
    for i in range(len_pattern):
        value = (total_char * value + ord(pat[i])) % modulo
        temp = (total_char * temp + ord(txt[i])) % modulo
    
    for i in range(len_string - len_pattern + 1):
        if value == temp:
            for j in range(len_pattern):
                if txt[i + j] != pat[j]:
                    break
            j += 1
            if j == len_pattern:
                print(f"pattern found at index {i}")
                flag = 1
        
        if (i < len_string - len_pattern):
            temp = (total_char * (temp - ord(txt[i]) * hash_) + ord(txt[i + len_pattern])) % modulo
            
            if (temp < 0):
                temp += modulo
    else:
        if (flag == 0):
            print("pattern not found")
        
if __name__ == "__main__":
    txt = input()
    pat = input()
    modulo = 103
    search(pat, txt, modulo)


