# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:41:38 2020

@author: Abhijit
"""

rnum=int(input("Enter your Roll Number:"))

if rnum<5 :
    print("You are in Group 1 ")
    
elif rnum==5 or rnum==6 or rnum==7 or rnum==8 :
    print("You are in Group 2")
    
elif rnum==9 or rnum==10 or rnum==11 or rnum==12 :
    print("You are in Group 3")
    
elif rnum==13 or rnum==14 or rnum==15 or rnum==16 :
    print("You are in Group 4")

elif rnum>16 :
    print ("You are in Group 5")
    


