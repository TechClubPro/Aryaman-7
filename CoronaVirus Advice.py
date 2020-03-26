# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:02:20 2020
CoronaVirus Test 
@author: Aryaman
"""
# Variables 

Q=0

Yes=0


# Questions

while Q<=4 :
    Q=Q+1
    
    if Q==1:
       ans=input("Do you have cough:")
       if ans=='yes' or ans=="Yes" or ans=="YES" or ans=="YEs" :
           Yes=Yes+1
       
           
            
     
    if Q==2 :
         ans=input("Do you have fever:")
         if ans=='yes' or ans=="Yes"  or ans=="YES" or ans=="YEs" :
           Yes=Yes+1
         
         
    if Q==3:
       ans=input("Do you have breathing problems:")
       if ans=='yes' or ans=="Yes"  or ans=="YES" or ans=="YEs":
           Yes=Yes+1
      
    if Q==4:
        ans=input("Do you have Fatigue and body Aches:")
        if ans=='yes' or ans=="Yes"  or ans=="YES" or ans=="YEs":
              Yes=Yes+1
        
                 
       
     

if Yes>=3 :
    print ("You should have a CoronaVirus Test Done Now!")
if Yes ==1 or Yes==2 :
    print ("You should visit a doctor as soon as possible.")
if Yes==0 :
    print ("You are healthy and well")
 
        
       
        
