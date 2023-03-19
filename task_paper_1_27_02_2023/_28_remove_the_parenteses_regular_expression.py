# 28. Write a Python program to remove the parentheses area in a string using Regular Expression Sample data : ["example (.com)", "MSys", "github (.com)", "keka (.com)"] 
# Expected Output: 
# Example 
# MSys 
# github 
# keka


import re
items = ["Example(.com)", "MSys", "github (.com)", "keka (.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))