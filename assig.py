# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:08:05 2021

@author: jkfra
"""
def count(listOfTuple):
	
	flag = False

	# To append Duplicate elements in list
	coll_list = []
	coll_cnt = 0
	for t in listOfTuple:
		
		# To check if Duplicate exist
		if t in coll_list:
			flag = True
            
			continue
		
		else:
			coll_cnt = 0
			for b in listOfTuple:
				if b[0] == t[0] and b[1] == t[1]:
					coll_cnt = coll_cnt + 1
			
			# To print count if Duplicate of element exist
			if(coll_cnt > 1):
				print(t, "-", coll_cnt)
			coll_list.append(t)
					
	if flag == False:
		print("No Duplicates")

def removeDuplicates(listOfTuple):
    return list(set([i for i in listOfTuple]))


listOfTuple = [(1, 5), (6, 9), (1, 8), (6,9), (9,0) , (6,9)]
print(listOfTuple)
count(listOfTuple)          #Counting the occurance of the tuple 
print(removeDuplicates(listOfTuple))    #removing the duplicate









