# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:51:46 2020
Weesh Woosh Game
@author: Aryaman
"""

count =0

while count<50 :
    count = count+1
    
    if count%3==0 and count%5==0 :
        print ("Weesh Woosh")
        
    elif count%3==0 :
        print ("Weesh")
        
    elif count%5==0 :
        print ("Woosh")
        
    else :
        print (count)

    
