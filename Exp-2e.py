# -*- coding: utf-8 -*-
"""

Write a menu-driven program to demonstrate the use of dictionary in
python:
i) Create key/value pair dictionary.
ii) Update/concatenate and delete item from existing
dictionary.
iii) Find a key and print its value.
    
"""
while True:
    print("\n")
    print("Menu Driven Program")
    print("1. Print out the Dictionary: ")
    print("2. Update your Dictionary: ")
    print("3. Find a key & print value: ")
    print("4. concatenate and delete the dictionary: ")
    print("5. Exit ")
    choice = int(input("Enter your Choice: "))
    my_dict = {"Name": "Tom","Address": "Mumbai","Age": "19"}
    my_dict1 = {"Car":"Mercedes-AMG","Model":2020,"Class":"A-Class"}
    
    if choice == 1:
        print("-"*30+"Dictionary-1"+"-"*30)
        print(my_dict)
        print("-"*30+"Dictionary-2"+"-"*30)
        print(my_dict1)
    
    elif choice == 2:
        my_dict["Name"] = "Frason"
        my_dict["Address"] = "Pune"
        print(my_dict)
        
    elif choice == 3:
        print("Name: ",my_dict['Name'])

    elif choice == 4:
        print("My dictionary1: ",my_dict)
        print("My dictionary2: ",my_dict1)
        my_dict.update(my_dict1)
        print("Final Dict after Concat: ",my_dict)
        key_to_del = input("Enter the key to delete: ")
        if key_to_del in my_dict:
            del my_dict[key_to_del]
        else:
            print("Enter a valid key.")
        print("Final Dict: ",my_dict)
        
        
    elif choice == 5:
        break
        
    else:
        print("You entered wrong choice")
    
        
        
#Update/concatenate and delete item from existing dict






