'''1. Write a program in Python to find second highest number in an integer array
# without using inbuilt functions.'''

def calcu_largest(largest_):
    first_largest=largest_[0]
    for i in range(len(largest_)):
        if largest_[i] > first_largest:
            first_largest=largest_[i]
    

    second_largest=largest_[0]
    for i in range(len(largest_)):
        if largest_[i] > second_largest and largest_[i] != first_largest:
            second_largest = largest_[i]
    return second_largest


print(calcu_largest([10, 40, 50, 25, 45]))