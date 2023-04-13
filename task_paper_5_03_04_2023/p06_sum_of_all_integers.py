'''6. Read a given file and extract the integers from each line, concatenate all the
integers present in the same line and print the sum of all these integers. 
eg: <File content>
He is 32 yrs old and his son is 7 yrs old . She is 27 yrs old and her daughter is 2 yrs old . 
Output : 599 ## calculation : Integers on Line 1 + Line 2 = 327 + 272 = 599'''

import re

# Open the file and read the lines
with open('integers.txt', 'r') as f:
    lines = f.readlines()

total = 0  # Running total of all integers

# Iterate over the lines and extract the integers
for line in lines:
    integers = re.findall(r'\d+', line)  # Extract all integers as a list of strings
    integers = [int(i) for i in integers]  # Convert the list of strings to a list of integers
    concatenated_integers = int(''.join(map(str, integers)))  # Concatenate all integers in the line
    total += concatenated_integers  # Add the concatenated integers to the running total

print(total)  # Print the total sum of all integers in the file