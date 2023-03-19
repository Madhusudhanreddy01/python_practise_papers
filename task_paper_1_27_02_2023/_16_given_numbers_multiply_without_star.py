'''16. Write a program to multiply two given number without using “*” operation and any in built 
function'''

def multiply(x, y):
    product = 0
    for i in range(y):
        product += x
    return product

# Example usage:
a = 5
b = 7
c = multiply(a, b)
print(c)  
# Output: 35

'''In this program, the multiply function takes two arguments x and y, and calculates their product using a loop. 
Specifically, it iterates y times and adds x to a running total (product) each time. 
After the loop completes, the final value of the product is returned as the result of the multiplication.

Note that this implementation assumes that both x and y are non-negative integers. 
It will not work correctly for other types of input. Also, keep in mind that this method of 
multiplication is not very efficient for large numbers, as it requires a loop to run a large number of times.'''

