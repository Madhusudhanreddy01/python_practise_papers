'''7. Reverse the below string without changing the position of special characters. 
s = "adfw$vf&yvy*ugv%uy"'''

input_str = "adfw$vf&yvy*ugv%uy"

special_chars = []
non_special_chars = []

for char in input_str:
    if  char.isalpha():
        non_special_chars.append(char)
    else:
        special_chars.append(char)

non_special_chars.reverse()


output_str = ""
for char in input_str:
    if  char.isalpha():
        output_str += non_special_chars[0]
        non_special_chars = non_special_chars[1:]

    else:
        output_str += special_chars[0]
        special_chars = special_chars[1:]

print(output_str)


print("---------------or---------------")

import string

s = "adfw$vf&yvy*ugv%uy"
l1 = list(s)
left = 0
right =len(l1)-1
while left<right:
    if l1[left].isalpha() and l1[right].isalpha():
        l1[left],l1[right] = l1[right],l1[left]
        left+=1
        right-=1
    elif l1[left] in string.punctuation:
        left+=1
    elif l1[right] in string.punctuation:
        right-=1
print("".join(l1))

print("---------------or---------------")

strSample='adfw$vf&yvy*ugv%uy'
 
#convert string into list
listSample=list(strSample)

print(listSample)
 
i=0
j=len(listSample)-1
print(j)
 
while i<j:
    if not listSample[i].isalpha():
        i+=1
    elif not listSample[j].isalpha():
        j-=1
    else:
        #swap the element in the list 
        #if both elements are alphabets
        listSample[i], listSample[j]=listSample[j], listSample[i]
        i+=1
        j-=1

#convert list into string 
#by concatinating each element in the list
strOut=''.join(listSample)
print(strOut)