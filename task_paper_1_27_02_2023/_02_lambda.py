'''2. What is the lambda function in python? Explain with examples. 
In Python, a lambda function (also known as an anonymous function) is a small, nameless function that can be defined in a single line of code. It's a way to create a function without using the def keyword, and is typically used when you need to create a function for a short-term or one-time use.
The general syntax for a lambda function is:
python:
lambda arguments: expression

where arguments are the function's input parameters, and expression is the operation to be performed on those arguments.
Here's an example of a lambda function that takes two arguments and returns their sum:
python
sum = lambda x, y: x + y
print(sum(3, 5))  
# Output: 8
In this example, we define a lambda function called sum that takes two arguments, 
x and y, and returns their sum. We then call the function with the arguments 3 and 5, which returns 8.
Another example of a lambda function is one that squares a number:
python
square = lambda x: x**2
print(square(4))  
# Output: 16

In this example, we define a lambda function called square that takes one argument, 
x, and returns the square of that number using the ** operator. We then call the 
function with the argument 4, which returns 16.
'''

sum = lambda x, y: x + y
print(sum(3, 5))  # Output: 8


square = lambda x: x**2
print(square(4))  
# Output: 16

