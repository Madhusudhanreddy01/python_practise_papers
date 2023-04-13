'''26. Print the pattern Pattern for the input : 3
”1
 
21*
 
”123

Note : Logic should also work for dynamic input - Ex: 5'''



n= int(input("Enter the number of rows to print pattern: "))
Result="*"

for i in range(1,n+1):
    for j in range(1,i+1):
        Result = str(j)+ Result
    if i%2 == 0:
        print(Result)
    else:
        print(Result[::-1])
    Result="*"


print("--------------------------or----------------------")

# n= int(input("Enter the number of rows to print pattern: "))
# Result="*"

# def revers(List):
#     t = ""
#     for i in List:
#         t = i + t
#     return t

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         Result = str(j)+ Result
#     if i%2 == 0:
#         print(Result)
#     else:
#         print(revers(Result))
#     Result="*"
