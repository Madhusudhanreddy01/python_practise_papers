'''9. Given a list [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90] find the difference 
between the  length of the list and the count of unique elements in the list.'''

# Define the list
my_list = [1, 2, 1, 5, 9, 10, 2, 2, 7, 5, 3, 10, 8, 9, 15, 17, 21, 16, 17, 90]

# Find the difference between the length of the list and the count of unique elements
result = len(my_list) - len(set(my_list))

# Print the result
print(f"The difference between the length of the list and the count of unique elements is {result}")
