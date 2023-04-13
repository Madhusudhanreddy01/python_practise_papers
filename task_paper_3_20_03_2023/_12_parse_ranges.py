'''12. Write a function called parse_ranges, which accepts a string containing ranges of
numbers and returns an iterable of those numbers.
Ex: >>> parse_ranges('1-2,4-4,8-13')
[1, 2, 4, 8, 9, 10, 11, 12, 13]'''


def parse_ranges(string_):
    string_=string_.split(',')
    print(string_)
    result=[]
    for i in string_:
        digits_=i.split('-')
        start=int(digits_[0])
        end=int(digits_[-1])+1
        result+=list(range(start, end))
    return result
str_='1-2,4-4,8-13'
print(parse_ranges(str_))