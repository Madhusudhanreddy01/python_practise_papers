'''12. Write a Python Program to Reverse the Content of a File.

Input :-
I am
new to this
world of
Python. 

Output :- 
Python. 
world of
new to this
I am'''

def last_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines[::-1]
lines=last_lines('content_reverse.txt')
for i in lines:
    i=i.replace("\n","")
    print(i)