# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:54:05 2020

@author: Abhijit
"""

print ("Welcome To World Bank")

c=input("Enter your name ")
a=int(input("Enter your account number"))
b=int(input("Enter your password"))
if b==5624 :
    print ("Welcome" + str(c))
    
    print ("What transaction do you want to perform")

    print ("Balence Inquiry")
    print("Cash Deposit")
    print("Cash Withdrawal")
    print("Loan")
    balance=56000 
    d=int (input("Enter Transaction Number eg-1=Balance Inquiry "))
    if d==1 : 
        print ("Your Current Account balence is " + str(balance))
        
    if d==2 :
        h=int(input("How much amount do you want to deposit:"))
        print ("Your Balance is " + str(balance + h))
            
    if d==3 :
       i=int (input (" How much amount do you want to withdraw:"))
       print ("Your balance is " + str (balance-i))
       
    if d==4 :
        j=int(input("What amount Loan do you want:"))
        if balance/2 >= j :
        
            print ("Your loan has been sanctioned")
            k=input("Do you want the loan:")
            if k=='yes' or k=='Yes' :
                print ("Your balance now is" + str(balance + j))
            else :
                print ("Your balance is " + str(balance))
        else :
            print ("The amount is too high")
    
elif b==1234 :
    print ("Welcome" + str(c))
    
    print ("What transaction do you want to perform")

    print ("Balence Inquiry")
    print("Cash Deposit")
    print("Cash Withdrawal")
    print("Loan")
    balance=60000
    e=int (input("Enter Transaction Number eg-1=Balance Inquiry "))
    if e==1 : 
        print ("Your Current Account balence is " + str(balance))
        
    if e==2 :
        h=int(input("How much amount do you want to deposit:"))
        print ("Your Balance is " + str( balance + h))
            
    if e==3 :
       i=int (input (" How much amount do you want to withdraw:"))
       print ("Your balance is " + str (balance-i))

    if e==4 :
        j=int(input("What amount Loan do you want:"))
        if j<=balance/2 :
            print ("Your loan has been sanctioned")
            k=input("Do you want the loan:")
            if k=='yes' or k=='Yes' :
                print ("Your balance now is" + str(balance + j))
            else :
                print ("Your balance is " + str(balance))
        else :
            print ("The amount is too high")
    
elif b==3468 :
    print ("Welcome" + str(c))
    
    print ("What transaction do you want to perform")

    print ("Balence Inquiry")
    print("Cash Deposit")
    print("Cash Withdrawal")
    print("Loan")
    balance=100000
    f=int (input("Enter Transaction Number eg-1=Balance Inquiry "))
    if f==1 : 
        print ("Your Current Account balence is " + str(balance))
        
    if f==2 :
        h=int(input("How much amount do you want to deposit:"))
        print ("Your Balance is " + str(balance+h))
            
    if f==3 :
        i=int (input (" How much amount do you want to withdraw:"))
        print ("Your balance is " + str( balance-i))
        
    if f==4 :
        j=int(input("What amount Loan do you want:"))
        if j<=balance/2 :
            print ("Your loan has been sanctioned")
            k=input("Do you want the loan:")
            if k=='yes' or k=='Yes' :
                print ("Your balance now is" + str(balance + j))
            else :
                print ("Your balance is " + str(balance))
        else :
            print ("The amount is too high")

     
    
elif b==8906 :
    print ("Welcome"+ str(c))
    
    print ("What transaction do you want to perform")

    print ("Balence Inquiry")
    print("Cash Deposit")
    print("Cash Withdrawal")
    print("Loan")
    balance=60000
    e=int (input("Enter Transaction Number eg-1=Balance Inquiry "))
    if e==1 : 
        print ("Your Current Account balence is " + str(balance))
        
    if e==2 :
        h=int(input("How much amount do you want to deposit:"))
        print ("Your Balance is " + str( balance + h))
            
    if e==3 :
       i=int (input (" How much amount do you want to withdraw:"))
       print ("Your balance is " + str (balance-i))

    if e==4 :
        j=int(input("What amount Loan do you want:"))
        if j<=balance/2 :
            print ("Your loan has been sanctioned")
            k=input("Do you want the loan:")
            if k=='yes' or k=='Yes' :
                print ("Your balance now is" + str(balance + j))
            else :
                print ("Your balance is " + str(balance))
        else :
            print ("The amount is too high")
    
  
else :
    print ("Incorrect Password")
    
