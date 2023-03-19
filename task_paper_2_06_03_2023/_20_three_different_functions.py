'''20. You are given a string having alphabets,digits,special characters. Write three different functions  to extract the digits[should be in sorted order], special character & vowels[should be in reverse]  from the given string. 
i/p string : "abcd123bye09@8" 
o/p: digits - 012389 
 special character - @ 
 vowels - ea 
'''


def extract_digits(input_str):
    digits = [char for char in input_str if char.isdigit()]
    digits = sorted(set(digits))
    return ''.join(digits)

def extract_special_characters(input_str):
    special_chars = [char for char in input_str if not char.isalnum()]
    return ''.join(special_chars)

def extract_vowels(input_str):
    vowels = [char for char in input_str if char.lower() in 'aeiou']
    vowels = vowels[::-1]
    return ''.join(vowels)
input_str = "abcd123bye09@8"
digits = extract_digits(input_str)
special_chars = extract_special_characters(input_str)
vowels = extract_vowels(input_str)

print("Digits:", digits)
print("Special characters:", special_chars)
print("Vowels:", vowels)