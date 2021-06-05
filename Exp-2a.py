lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Orignal list: ",lst)
print("-"*50)
even_lst = list(filter(lambda x : x % 2 == 0, lst))
print("even numbers :",even_lst)        #number that is even
print("sum of even numbers: ",sum(even_lst))          #sum of even numbers
odd_lst = list(filter(lambda x : x %2 != 0, lst))
print("-"*50)
print("odd numbers: ",odd_lst)              #number that is odd
print("sum of odd numbers: ",sum(odd_lst))
#count the number of element which is divisible by 3
div_three = list(filter(lambda x: x % 3 == 0, lst))
print("Count of number divisible by three: ",len(div_three))  #giving the no. % by 3 and the count of the no.
print("-"*50)
lst.extend([11,12,13,14,15])        #inserting element in a list
print("Extended list: ",lst)
print("-"*50)
del(lst[::2])               #deleting all the odd numbers from the list
print("list after elements deleted: ",lst)








