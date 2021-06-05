# -*- coding: utf-8 -*-
"""

Write a menu-driven program to demonstrate the use of set in
python:
i) Accept two strings from the user.
ii) Display common letters in two input strings (set
intersection).
iii) Display letters which are in the first string but not in
the second string (set difference).
iv) Display set of all letters from both the strings (set
union).
v) Display set of letters which are in two strings but not
common (Symmetric Difference).


"""

while True:
    print("Menu Driven Program")
    print("1. Enter string: ")
    print("2. Common letters String: ")
    print("3. Set diffrence in String: ")
    print("4. Set Union in String: ")
    print("5. Symmetric Diffrence: ")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        str1 = set(input("Enter string 1: "))
        str2 = set(input("Enter string 2: "))
        
    elif choice == 2:
        a = list(set(str1)&(set(str2)))
        print("The common letters are: ")
        for i in a:
            print(i)
            
    elif choice == 3:
       z = str1.difference(str2)
       print("Set diffrence: ",z)  
        
    elif choice == 4:
        uno = set(str1).union(str2)
        print("set union: ",uno)
       
    elif choice == 5:
        sym = str1.symmetric_difference(str2)
        print("symmetric diffrence: ",sym)
        
    if choice == 6:
        break
            
        
        
        
