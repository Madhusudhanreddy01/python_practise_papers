# 4. In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out  all the keys 
#    in a list named as ‘list_keys’ and list out all the values in a list named as ‘list_values’.  
# Also find out the value of key ‘Australia’ in the list and as it is not existing in the list print ‘NA’ as  its value.


# Define the dictionary
my_dict = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'Nepal': 'Kathmandu'}

# Get all the keys in a list
list_keys = list(my_dict.keys())
print("Keys: ", list_keys)

# Get all the values in a list
list_values = list(my_dict.values())
print("Values: ", list_values)

# Get the value of key 'Australia' in the dictionary
value = my_dict.get('Australia', 'NA')
print("Value of 'Australia': ", value)
