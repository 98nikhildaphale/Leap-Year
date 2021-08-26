# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x=int(input("Ënter a year: "))


if x%4==0 and x%100!=0:
    print(" It is a Leap year")
elif x%400==0:
    print("It is a Leap year")    
else:
    print(" It is not a Leap year")
    