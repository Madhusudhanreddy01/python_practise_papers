'''14. When do you use generators in python? Give an example 
A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values. In a generator function, a yield statement is used rather than a return statement.
The following is a simple generator function. 
#Example:'''

def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

'''In the above example, the mygenerator() function is a generator function. 
It uses yield instead of return keyword. So, this will return the value against 
the yield keyword each time it is called. However, you need to create an iterator 
for this function, as shown below.'''
    
gen = mygenerator() 
print(next(gen)) 
# First item 
10                      
print(next(gen)) 
# Second item 
20                      
print(next(gen)) 
# Last item 
30                      