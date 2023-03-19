'''16. Write a function which will take a string argument and reverse the words in 
the string. For  example – Input string -- “Hello World”. Output should be “olleH dlroW”. '''

word="Hello World".split(" ")

def fun(arg):
   result=""
   for i in arg:
       result=result+(i[::-1])+" "
   return result
print(fun(word))