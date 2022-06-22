# -*- coding: utf-8 -*-
"""
Created on Wed May 18 09:24:53 2022

@author: c_con
"""

def convertToStr(num):
    conv = str(num)
    if Palindrome(conv):
        print(conv + " is a Palindrome")
    else:
        print(conv + " is not a Palindrome")
    
def Palindrome(num1):
    if len(num1) > 1:
        if num1[0] == num1[-1]:
            return Palindrome(num1[1:-1])
        else:
            return False
    else:
        return True
    
convertToStr(int(input("input a whole number: ")))