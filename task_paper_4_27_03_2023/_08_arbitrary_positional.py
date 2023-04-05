# 8. What is the return type of arbitrary positional arguments and arbitrary keyword arguments.

def positional_(*args):
    results_=0
    for i in args:
        results_ += i
    return results_
print(positional_(1,2,3,4))

def keyword_(**kwargs):
    result=0
    for i in kwargs.values():
        result += i
    return result
print(keyword_(a=1, b=2, c=3, d=4, e=5))