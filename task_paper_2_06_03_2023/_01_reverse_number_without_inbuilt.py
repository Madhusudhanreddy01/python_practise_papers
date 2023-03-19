# 1. Write a program to reverse a number without using any inbuilt function.

# num=input()
# reverse_=num[::-1]
# print(reverse_)


number = int(input("enter the number: "))
rev_num=0
for digit in range(len(str(number))):
    rev_num = rev_num * 10 + number % 10
    number //= 10
print(f"After reversed number is {rev_num}")