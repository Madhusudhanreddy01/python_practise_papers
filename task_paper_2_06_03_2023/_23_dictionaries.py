# 23. create 2 dictionaries as follows: 
# dict1 = {'name': 'Msys', 'Place': 'Pune'} 
# dict2 = {'EmpID': 0001, 'Salary': 50000} 
# Perform following operations: 
# a. create single dictionary by merging dict1 & dict2 
# b. update the salary to 10% 
# c. update age to 35 
# d. extract & print all the values & keys separately in tuple. 
# e. delete the element with key 'Age' & print the dictionary elements.




dict1 = {"name": "Msys", "Place": "Pune"} 
dict2 = {"EmpID": 1, "Salary": 50000} 

#way1
dict1.update(dict2)
print(dict1)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#way2
merge_dict=({**dict1,**dict2})
print(merge_dict)
print("-------------------------------------------------")

#update the salary
present_salary=merge_dict["Salary"]
updates_salary = (present_salary + (present_salary * 0.1))
print(updates_salary)
print("-------------------------------------------------")

#add age:
merge_dict["age"]=35
print(merge_dict)
print("-------------------------------------------------")

#values,keys
print(tuple(merge_dict.keys()))
print(tuple(merge_dict.values()))
print("-------------------------------------------------")

#delete age:
del merge_dict["age"]
print(merge_dict)