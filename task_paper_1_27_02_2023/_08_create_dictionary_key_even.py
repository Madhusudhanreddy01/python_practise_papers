'''8. Create a dictionary where the key is an even number from the given list and the value 
will be the occurrence of that element in the list. input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]'''


input_= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]
set_=set(input_)
list_1=[]
list_2=[]
for i in set_:
  if (i%2==0):
    c= input_.count(i)
    list_1.append(i)
    list_2.append(c)
z=zip(list_1,list_2)
print(dict(z))