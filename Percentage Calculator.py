# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:09:07 2020
Percenatge Calculator
@author: Aryaman
"""
# Variables

q=0
marks=0

while q<=5 :
    q=q+1
    
    if q==1 :
        a=int(input("Enter your marks in English out of 100:"))
        marks=marks+a
        
    if q==2 :
        b=int(input("Enter your marks in Science out of 100: "))
        marks=marks+b
        
    if q==3 :
        c=int(input("Enter your marks in Maths out of 100: "))
        marks=marks+c
        
    if q==4 :
        d=int(input("Enter your marks in History out of 100: "))
        marks=marks+d
        
    if q==5 :
        e=int(input("Enter your marks in Geography out of 100: "))
        marks=marks+e
        
print("Your Score in Percentages is " + str (marks/500*100))

if marks/500*100 <35 :
    print ("Fail")
    
elif marks/500*100 >35 and marks/500*100<45 :
    print ("3rd Division")
    

elif marks/500*100 >45 and marks/500*100<60 :
    print ("2nd Division")
    
elif marks/500*100 >60 and marks/500*100<75 :
    print ("1st Division")
    
elif marks/500*100 >75 :
    print ("Distinction")
    