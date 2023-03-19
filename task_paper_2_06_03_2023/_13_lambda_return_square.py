# 13. Write a lambda function which takes two input arguments x and y. If x is greater than y then it  should return square of y and if y is greater than x, 
# then it should return square of x. 

i=10
j=20 
if(i>j):
    x=lambda i:i**2
    print("i is greater : "+str(x(i)))
else:
    y=lambda j:j**2
    print("j is greater : "+str(y(j)))