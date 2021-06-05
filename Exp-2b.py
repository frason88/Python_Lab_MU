"""

Write a python program to input a multiline string or a paragraph & 
count the no. of words & characters in string. Also check for a substring & 
replace each of its occurrences by some other string. 

"""


lines = []
#Getting multi-line input from the user
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
print('-'*80)
print(text)

# word count
total_char = 0                      #total char
total_w = 1                         #total words
for i in range(len(text)):
    if(text[i] == ' ' or text[i] == '\n'):
         total_w += 1         
print("Total no. of words: ",total_w)

#char count
for j in range(len(text)):
    total_char += 1
print("The total number of characters: ",total_char)


# print("Final list: ",lines)




# Driver Code 
x = input("Enter the word you wanna replace: ")


def countX(text, x): 
    return text.count(x)

#occurance count

print('{} has occurred {} times: '.format(x, countX(text, x))) 

print("------------------The new string after occurance----------------------")

string_replace = text.replace("Python", "Java")

print(string_replace)










