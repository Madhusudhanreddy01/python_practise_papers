'''5. From given list of numbers, create a list of square of prime numbers .
l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]'''

l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]
l2 = []
for i in l1:
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            l2.append(i**2)
print(l2)

print("-----------------------or----------------------")

import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

# numbers=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]

numbers=[1, 4, 6, 11, 15, 24, 19, 25, 27, 30,17]

squares_of_primes=[num ** 2 for num in numbers if is_prime(num)]

print(squares_of_primes)
