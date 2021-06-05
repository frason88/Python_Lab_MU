# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:29:39 2021

@author: jkfra
"""
import math

print("Enter the first point A")
x1, y1 = map(int, input().split())

print("Enter the second point B")
x2, y2 = map(int, input().split())

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("The Euclidean Distance is " + str(dist))