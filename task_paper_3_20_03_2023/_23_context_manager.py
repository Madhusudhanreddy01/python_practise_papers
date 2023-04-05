'''23. Create a context manager. Context managers use a with block to bookend a block of code 
with automatic setup and tear down steps.Your context manager, suppress, should suppress 
exceptions of a given type:
 >>> with suppress(NameError): 
... print("Hi!") 
... print("It's nice to meet you,", name) 
... print("Goodbye!") 
... 
Hi! 
But exceptions of other types shouldn't be suppressed (we're suppressing a TypeError and a 
NameError is raised): 
>>> with suppress(TypeError): 
... print("Hi!") 
... print("It's nice to meet you,", name) 
... print("Goodbye!") 
... 
Hi! 
Traceback (most recent call last): 
File "", line 3, in <module>
NameError: name 'name' is not defined '''


class suppress:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return self
    
    def __exit__(self, exc_value, exc_tb):
        if isinstance(exc_value, self.exc_type):
            return True
        
with suppress(NameError):
    print("Hi!")
    print("It's a nice to meet you,", name)
    print("Goodbye!")

with suppress(TypeError):
    print("Hi!")
    print("It's a nice to meet you,", name)
    print("Goodbye!")