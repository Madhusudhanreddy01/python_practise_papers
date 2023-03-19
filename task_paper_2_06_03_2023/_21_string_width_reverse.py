'''21. You are given a string and width. Your task is to wrap the string into paragraph of width in  reverse order. Blank spaces should be ignored. 
for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this  organisation. 
 the second line contains the width - 4 
 o/p 
lleH 
ew,o 
mocl 
tote 
osih 
nagr 
tasi 
.noi
'''

string = "Hello, welcome to this organisation."
width = 4

# Reverse the string and remove blank spaces
string = string[::-1].replace(" ", "")
# print(string)

# Wrap the string into paragraphs of width and reverse each line
paragraphs = [line[::1] for line in [string[i:i+width] for i in range(0, len(string), width)][::-1]]

# Print the paragraphs
for line in paragraphs:
    print(line)
