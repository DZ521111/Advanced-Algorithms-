# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:14:36 2020

@author: DHRUV
"""
import random as rn

def find_gcd(num1, num2):
    if (num1 < num2):
        return (find_gcd(num2, num1))
    elif (num1 % num2 == 0):
        return num2
    else:
        return ((find_gcd(num2, num1 % num2)))
    
def find_power(a, num1, num2):
    result = 1
    a = a % num2
    while(num1 > 0):
        if (num1 & 1):
            result = (result * a) % num2
        num1 = num1 // 2
        a = (a ** 2) % num2
    return result

def isprime(num):
    k = 10
    if (num <= 1 or num == 4):
        return False
    if (num <= 3):
        return True
    while (k > 0):
        r = rn.randint(2, num-1)
        if (find_gcd(num, r) != 1):
            return False
        if (find_power(r, num - 1, num) != 1):
            return False
        k -= 1
    return True
        
if __name__ == "__main__":
    num = int(input("Enter the large number : "))
    if (isprime(num)):
        print(f"{num} is prime!")
    else:
        print(f"{num} is composite")
        
        
        