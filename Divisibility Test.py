# -*- coding: utf-8 -*-
"""
Spyder Editor


Find if a number is divisible by another number 

This is a temporary script file.
"""
#Variables 

FirstNum=0
NumDivBy=0

#Input Statements

FirstNum=int (input("Enter First Number:"))
NumDivBy=int (input("Enter a number to check if the first number is divisible by it:"))

#If Else Statements 

if FirstNum%NumDivBy == 0 :
    print (str(FirstNum) + (" is divisible by ") + str( NumDivBy))
    
else :
    print (str(FirstNum ) + (" is not divisible by " ) + str(NumDivBy))
    
         
