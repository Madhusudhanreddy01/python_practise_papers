# 20. Write a python program for sort the given below list based last character of each word 
# names_list = ['Prabhu', Rahul', 'Arunesh, 'Sonali', 'Rakshit']


names_list = ['Prabhu', 'Rahul', "Arunesh","Sonali","Rakshit"]
list_=[]
list_1=[]
for i in names_list:
      c=[i[-1],i]
    #   key (h), value(Arunesh)
      list_.append(c)
      list_1.append(i[-1]) #actual keys ni sort cheyadaniki separte
      
x=dict(list_)
sort=sorted(list_1)
sorted_list=[]
for i in sort:
    sorted_list.append(x[i])
print(names_list)
print(sorted_list)

# ------------------------------------------------
# names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']

# sorted_list = sorted(names_list, key=lambda x: x[-1])

# print(sorted_list)

# ------------------------------------------------------
# Define a function to get the last character of a string
def last_char(word):
    return word[-1]

# Define the list of names
names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']

# Sort the list based on the last character of each word
sorted_names = sorted(names_list, key=last_char)

# Print the sorted list
print(sorted_names)
