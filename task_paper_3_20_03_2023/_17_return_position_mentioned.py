'''17. Write a function that takes a sequence (like a list, string, or tuple) and a number n
and returns the last n elements from the given sequence, as a list. For example:
>>> tail([1, 2, 3, 4, 5], 3)
[3, 4, 5]'''

def tail(seq, n):
    return list(seq[-n:])

list_=list(map(int, input().split()))
pos_=int(input())
print(tail(list_, pos_))