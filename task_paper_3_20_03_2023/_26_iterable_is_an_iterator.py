'''26. Write a function so that it accepts an iterable and returns True if the given iterable
is an iterator.'''

def is_iterator(iterable):
    if iter(iterable) is iterable:
        return True        
   
print(is_iterator(iter([]))) 
print(is_iterator([1,2,3]))