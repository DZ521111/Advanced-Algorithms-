# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:49:35 2020

@author: DHRUV
""" 
total_char = 256

def search(pat, txt, q): 
    
        len_pattern = len(pat) 
    	len_string = len(txt)
    	i, j, value, temp, hash_ = 0, 0, 0, 0, 1 
    	for i in range(len_pattern-1): 
        	hash_ = (hash_ * total_char) % q 
   
    	for i in range(len_pattern): 
        	value = (total_char * value + ord(pat[i])) % q 
        	temp = (total_char * temp + ord(txt[i])) % q 
        
    	for i in range(len_string - len_pattern + 1): 
        	if value == temp: 
            	for j in range(len_pattern): 
                	if txt[i + j] != pat[j]: 
                    	break
  
                j += 1
                if j == len_pattern: 
                    print (f"Pattern found at index {i}" ) 
  
            if i < len_string - len_pattern: 
                temp = (total_char * (temp - ord(txt[i]) * hash_) + ord(txt[i +len_pattern])) % q 

            if temp < 0: 
                temp = temp + q
    	    else:
        	    print("pattern Not found!")

if __name__ == "__main__":   
    	txt = input("Enter the string : ")
    	pat = input("Enter the pattern : ")
    	q = 103
    	search(pat,txt,q)
