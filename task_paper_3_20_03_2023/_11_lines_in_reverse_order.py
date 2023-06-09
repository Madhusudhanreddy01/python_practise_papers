'''11. Write a function, last_lines, which returns lines in a given ASCII text file in
reverse order.
For example, given the following file, my_file.txt:
This is a file
This is line 2
And this is line 3
The last_lines function should work like this:
>>> for line in last_lines('my_file.txt'):
... print(line, end='')
...
And this is line 3
This is line 2
This is a file'''


def last_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines[::-1]
lines=last_lines('lines_reverse.txt')
for i in lines:
    i=i.replace("\n","")
    print(i)