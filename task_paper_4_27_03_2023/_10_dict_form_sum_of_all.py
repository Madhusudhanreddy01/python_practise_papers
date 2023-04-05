# 10. Generate a dictionary from the two given lists using dict function (without using for loops) and calculate the sum of all the values in the dictionary using reduce and anonymous concepts
# L1 = [“a”,”b”]	
# L2 = [1,2] 
# Expected Output : data = {“a'.1, “b'.2} sum = 3

from functools import reduce
l1=['a','b']
l2=[1,2]
my_dict=dict(zip(l1,l2))
total_sum=reduce(lambda x,y: x+y, my_dict.values())
print(my_dict)
print(total_sum)