# 17. Write a program to find the count of alphabet alone in the given alphanumeric string for 
# Ex1: input=’abb24ccc8ddbbca1’ output=’a1b224c3d2b2c1a11’ 
# Ex2: input = ‘abc23’ output=’a1b1c123’

input1=input("Enter:")
n = len(input1)
output=''
count=1

for i in range(n):
    if input1[i].isalpha() and input1[i] == input1[i + 1]:
        count += 1

    elif input1[i].isalpha() and input1[i] != input1[i + 1]:
        output+=input1[i]+str(count)
        count = 1

    elif input1[i].isdigit:
        output+=input1[i]
print(output)