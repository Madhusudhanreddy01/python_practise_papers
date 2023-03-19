'''2. Given a list of first 10 natural numbers, write a program to find the square 
of all even numbers  and cube of all odd numbers and store them in another list.'''

numbers = [1,2,3,4,5,6,7,8,9,10]   
result_square = []
result_cube = []                                 

for num in numbers:                         
    if num % 2 == 0:                        
        square = num ** 2               
        result_square.append(square)       
    else:                                   
        cube = num ** 3                     
        result_cube.append(cube)                 

print("square root of even no:", result_square)    
print("cube root of odd no:", result_cube)
