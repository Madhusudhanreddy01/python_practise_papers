# 15. Define logic for generating the random password with the provided length as an input.

import  random


caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
special_char = "!@#$%^&*"
n= int(input("Enter digit to generate Password: "))
password=''
for i in range(n):
    password+=random.choice(caps+small+number+special_char)
print(f'Your Password is:',password)
