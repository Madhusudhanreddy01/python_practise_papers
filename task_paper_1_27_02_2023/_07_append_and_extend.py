'''7. Difference between append and extend operations of list 
Both append and extend are list methods in Python that allow you to add items to a list. 
However, there is a difference in how they add elements to the list.
append method adds a single element to the end of the list.
For example:
Python'''
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)   
# Output: [1, 2, 3, 4]

'''In this example, the append method adds the integer value 4 to the end of the list my_list.
extend method, on the other hand, allows you to append multiple items to the end of the list. 
It takes an iterable (e.g., a list, tuple, or set) as an argument and adds each element of the 
iterable to the list individually.
For example:
python'''
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)   
# Output: [1, 2, 3, 4, 5, 6]

'''In this example, the extend method adds three new elements (4, 5, and 6) to the end of the list my_list.
In summary, append adds a single element to the end of the list, 
while extend adds multiple elements to the end of the list by taking an iterable as an argument.'''
