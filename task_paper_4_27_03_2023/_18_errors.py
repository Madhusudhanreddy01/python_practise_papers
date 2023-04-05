# 18. Write sample code for reproducing the below errors and print the user defined messages with the 
# use of exception handling concept 
# • IndexError,TypeError,AttributeError,ValueError

print("-----------------------------------------------------")
# Index Error
try:
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError:
    print("Error: The index you entered is out of range")

print("-----------------------------------------------------")
# Type Error
try:
    my_num = 123
    my_str = "hello"
    print(my_num + my_str)
except TypeError:
    print("Error: The types of the two variables are incompatible")

print("-----------------------------------------------------")
# Attribute Error
try:
    my_dict = {"name": "John", "age": 30}
    print(my_dict.city)
except AttributeError:
    print("Error: The attribute you are trying to access does not exist")

print("-----------------------------------------------------")
# Value Error
try:
    my_num = int("hello")
except ValueError:
    print("Error: The value you entered is not valid for conversion to an integer")

print("-----------------------------------------------------")