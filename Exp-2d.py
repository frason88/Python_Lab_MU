# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:04:37 2021

@author: jkfra
"""
name = str(input('Enter the name of the student: '))
  

while True:
    print('Menu Driven Program: ')
    print("1. Add Student Marks: ")
    print("2. Student admission Date in the form (dd/mm/yyyy): ")
    print("3. Display Student Info: ")
    print("4. Exit \n")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        std_mks= tuple([eval(x) for x in input("enter the values: ").split(',')])
        sum_mks = print("The sum of marks: ",sum(std_mks))
        avg_mks = print("The average std marks: ",sum(std_mks)/len(std_mks))
        print("-"*60)
       
    elif choice == 2:
        std_dates = tuple([eval(x) for x in input("Enter the Date of Admission: ").split('/')])
        print("-"*60)
       
    elif choice == 3:
        #print("\n Name: {}\n Marks: {}\n Date: {}".format(name,std_mks,std_dates))
        data = [(name,std_mks,std_dates)]
        print(data)
        print("-"*60)
        
    else:
        print("Thank you \n")
        break
        


  
        
        
        
        
