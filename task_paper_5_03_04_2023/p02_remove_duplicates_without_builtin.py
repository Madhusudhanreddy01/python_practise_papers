'''2. Write a program in Python to remove duplicate elements form array without using
inbuilt function.'''

list_=[1,2,3,2,3,4,5,4,6]

list_2=[]

for i in list_:
    if i not in list_2:
        list_2+=[i]
print(list_2)