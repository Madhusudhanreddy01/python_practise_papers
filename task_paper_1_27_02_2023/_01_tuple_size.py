'''1. What are the differences between list and tuple? Which is faster and why? 
Lists are mutable, which means you can add, remove or modify elements in a list after it has been created. 
Lists are created using square brackets []. 
Lists are used when the order and/or number of elements may change during the program execution.

Tuples are immutable, which means you cannot change its contents once it has been created.
Tuples are created using parentheses ().
Tuples are used when you want to ensure that the contents of the collection remain the same throughout the program.

In terms of speed, 
tuples are generally faster than lists. This is because tuples are immutable, which allows the interpreter to optimize certain operations on them, such as indexing and iterating. 
Lists, on the other hand, are mutable, which makes them slower for certain operations.'''



# Which is faster and why?
# Ans: Tuple is faster because  Creating Tuple is faster than creating a list, Creating a list is slower because two memory blocks need to be accessed.

tuple_A = ('Name = kumar ' ,'Grade = 2','ID = 101', 'Section = A','gender=M')
list_B  = ['vegitables','fruits', 'books', 'pens','etc']

print("Tuple data is : ", tuple_A)
print("List data is : ", list_B)

print("size of a tuple is : ",tuple_A.__sizeof__())
print("size of a list is : ",list_B.__sizeof__())