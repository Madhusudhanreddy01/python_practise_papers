'''3. What is monkey patching and what is the use of monkey patch? 
What is this?
Monkey Patching is Providing capability of changing the behavior or modify the executing code at runtime.
Why is this?
Suppose you have a program to run but you won't have a different output. 
What you will do without changing the user code. That is why Monkey Patching here.
How is this?

Output: This is a Monkey function'''


class Test:
    def class_method(self):
        print("This is a class method")
def monkey_function():
    print("This is a Monkey function")

Test.class_method=monkey_function
Test.class_method()