# 3 Define logic for identifying the even numbers and odd numbers from the given list and generate a dictionary as follows
# numbers = [4,5,7,2,9,8]
# result	= (“even”:[4,2,8],”odd'.[5,7,9]}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
numbers_dict = {'Even': even_numbers, 'Odd': odd_numbers}
print(numbers_dict)