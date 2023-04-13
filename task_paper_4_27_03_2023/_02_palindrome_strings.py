'''2. Define a function which returns a list contains only the palindrome strings from the list of provided string elements
input	: List of strings
output : List of palindrome strings'''

def get_palindromes(strings):
    return[s for s in strings if s == s[::-1]]
my_strings=['racecar','level','python']
palindromes=get_palindromes(my_strings)
print(palindromes)

print("--------or---------------")

def palindrome_(_list):
    res=[]
    for i in _list:
        if i == i[::-1]:
            res.append(i)
    print(res)

list_=["racecar", "level", "python"]
palindrome_(list_)