'''30. How does the context manager work in python? Explain the internal methods. 
Write a custom sample context manager. 
Context managers allow you to allocate and release resources precisely when you want to. 
The most widely used example of context managers is the with statement. 
Suppose you have two related operations which you’d like to execute as a pair, 
with a block of code in between. Context managers allow you to do specifically that. 
For example:
with open('madhu.txt', 'w') as opened_file:
    opened_file.write('Msr!')

The above code opens the file, writes some data to it and then closes it. 
If an error occurs while writing the data to the file, it tries to close it. 
The above code is equivalent to:
file = open('madhu.txt', 'w')
try:
    file.write('Msr!')
finally:
    file.close()

While comparing it to the first example we can see that a lot of boilerplate code is 
eliminated just by using with. The main advantage of using a with statement is that it 
makes sure our file is closed without paying attention to how the nested block exits.
A common use case of context managers is locking and unlocking resources and closing 
opened files (as I have already shown you).'''

print("Implementing a Context Manager as a Class:")
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        # print("exception has been handled")
        self.file_obj.close()
        # return True

with File('context_class.txt', 'w') as opened_file:
    # opened_file.undefined_function('Madhusudhan')
    opened_file.write('Madhusudhan')

# ---------------------------------------------------------------
# class MyContextManager:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = None

#     def __enter__(self):
#         self.file = open(self.filename, 'w')
#         return self.file

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()

# with MyContextManager('context_class.txt') as f:
#     f.write('MSR')

#----------------------------------------------------------------------
# print("Implementing a Context Manager as a Generator.")

# from contextlib import contextmanager

# @contextmanager
# def open_file(name):
#     f = open(name, 'w')
#     try:
#         yield f
#     finally:
#         f.close()

# with open_file('some_file.txt') as f:
#     f.write('Madhusudhan')
