# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:28:52 2020

@author: DHRUV
"""
import numpy as np

def unique(pattern):
    x = np.array(list(pattern))
    return (np.unique(x))

string = input("Enter the string :- ")
pattern = input("Enter the pattern :- ")

smallest_char, len_pattern = min(pattern), len(pattern)
states, acceptstate = len_pattern + 1, len_pattern
distinct_ele = len(unique(pattern))

table = []
input_, __, curr_state = [], [0, 1, 2, 3], 0

for _ in range(states):     # Take input Table!
    input_ = []
    print(f"Current state : {_}\tInput : {__}\tNext state :")
    input_ = list(map(int, input().split()))
    table.append(input_)

print("\n")
for row in table:           # print Automata table!
    print(*row)

if (len(string) == 0):
    print("string not valid!")
else:
    for ___ in range(len(string)):
        dist = ord(string[___]) - ord(smallest_char)
        curr_state = table[curr_state][dist]
        if (curr_state == acceptstate):
            print(f"pattern found at index of : {___ - len_pattern + 1}")
            