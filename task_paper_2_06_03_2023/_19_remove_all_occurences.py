'''19. Write a function which takes input string from the user as argument and the character 
also taken  by the user as the argument and remove all the occurences of that 
character from the string. Also if  the given character is not present in the string 
your function should raise the exception stating that  “Given character is not present in the string. 
Please try with a new one”.'''

def remove_char(string, char):
    if char not in string:
        raise ValueError("Given character is not present in the string. Please try with a new one.")
    return string.replace(char, '')
string = input("Enter a string: ")
char = input("Enter a character to remove: ")
try:
    new_string = remove_char(string, char)
    print("New string:", new_string)
except ValueError as e:
    print(e)