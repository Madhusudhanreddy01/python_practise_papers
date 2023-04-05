'''18. Print the below rhombus pattern according to the given number 
for eg: given number is 4 then  
o/p will be  
         1 
        212 
       32123 
      4321234 
       32123  
        212  
         1 '''
n = int(input("Enter a number:"))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()
for i in range(n-1,0,-1):
    print(" " * (n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()

# ----------------------------------------------------------------

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(" "*(n-i) + "".join(str(j%10) for j in range(i, 0, -1)) + "".join(str(j%10) for j in range(2, i+1)) )

# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "".join(str(j%10) for j in range(i, 0, -1)) + "".join(str(j%10) for j in range(2, i+1)) )
