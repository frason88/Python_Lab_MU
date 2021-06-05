# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:12:47 2021

@author: jkfra
"""

def pow(x, y):
    if y == 1:
        return x
    else:
        return pow(x, y-1) * x
    
def fibSeries(num):  
    if num <= 1:
        return num
    else:
        return fibSeries(num-1) + fibSeries(num-2)

# main code
if __name__ == '__main__':
    
    x = int(input("Enter base term: ")) 
    y = int(input("Enter power term: "))  
    result = pow(x, y)
    print(x," to the power ", y, " is: ", result)


print("-"*50)

# take input
num = int(input('Enter number of terms for fib: '))

# print fibonacci series
if num <= 0:
        print('Please enter a positive integer')
else:
    print('The fibonacci series:')
    for i in range(num):
        print(fibSeries(i), end=' ')