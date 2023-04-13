'''22. Write a function is_iterator so that it accepts an iterable and returns True if the
given iterable is an iterator.
is_iterator(iter([]))
True
>>> is_iterator([1, 2])
False
'''

def is_iterator(iterable):
    try:
        iter(iterable)
        return iter(iterable) is iterable
    except TypeError:
        return False
    
print(is_iterator("madhusudhan"))
print(is_iterator(iter("madhusudhan")))

print(is_iterator([1,2,3]))
print(is_iterator(iter([])))

print(is_iterator({1:10, 2:20, 3:30}))
print(is_iterator(iter({1:20, 2:20, 3:30})))
