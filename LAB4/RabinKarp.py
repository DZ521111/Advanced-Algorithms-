# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:08:00 2020

@author: DHRUV B KAKADIYA
"""
''' Implementation of RabinKarp Algorithm! '''

class RabinKarp:
    
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern
        self.find_pattern()
        
    def hash_function(self, text):
        hash_ = 0
        for _ in range(len(text)):
            hash_ += ord(text[_]) ** _
        return hash_
    
    def comparison(self):
        for i in range(len(self.string) - len(self.pattern) + 1):
            if (self.hash_function(self.string[i : i + len(self.pattern)]) == self.hash_function(self.pattern)):
                if (self.string[i : i + len(self.pattern)] == self.pattern):
                    return i
        else:
            return -1
        
    def find_pattern(self):
        if (len(self.string) < len(self.pattern)):
            print("length of pattern is higher then text!")
            exit
        else:
            index_ = self.comparison()
            if (index_ != -1):
                print(f"pattern found at index : {index_}")
            else:
                print("pattern not found!")


if __name__ == "__main__":
    Text = input("Enter the Text : ")
    pattern = input("Enter the pattern : ")
    RabinKarp(Text, pattern)