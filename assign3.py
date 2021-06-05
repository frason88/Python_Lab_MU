# -*- coding: utf-8 -*-
"""
Created on Sat May  8 09:01:16 2021

@author: jkfra
"""

# Ensure all keys in dictionary list
# Using set() + chain.from_iterable() + get() + list comprehension
from itertools import chain

# initializing list
test_list = [{'frason' : 1, 
              'kevin' : 3},
			{'soundarya' : 4, 
            'ishika' : 6, 
            'alana' : 5},
			{'adnan' : 8}]
			
# printing original list
print("The original list is : " + str(test_list))

# extracting all keys
all_keys = set(chain.from_iterable(test_list))

# assigning None using get() if key's value is not found
res = [dict((key, sub.get(key, None)) for key in all_keys) for sub in test_list]

# printing result
print("Reformed dictionaries list : " + str(res))
        