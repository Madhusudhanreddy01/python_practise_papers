'''25. Write a program to convert integers to Roman numbers.'''

def int_to_roman(num):
    # Define mappings between decimal values and Roman numerals
    roman_map = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',
                 40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I' }
    roman_num = ""
    for value, numeral in roman_map.items():
        while num >= value:
            roman_num += numeral
            num -= value
    return roman_num


print(int_to_roman(1997))
# print(int_to_roman(8))

print("-------------------------------")

# def printRoman(number):
#     num = [1, 4, 5, 9, 10, 40, 50, 
#            90, 100, 400, 500, 900, 1000]
    
#     sym = ["I", "IV", "V", "IX", "X", "XL", "L",
#            "XC", "C", "CD", "D", "CM", "M"]
    
#     i = 12

#     while number:
#         div = number // num[i]
#         number %= num[i]

#         while div:
#             print(sym[i], end="")
#             div -= 1
#         i-= 1

# #Driver code

# if __name__ == "__main__":
#     number = 1997
#     print("Roman value is:", end=" ")
#     printRoman(number)