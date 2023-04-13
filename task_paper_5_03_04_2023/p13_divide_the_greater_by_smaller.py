'''13. Write a python program to take 2 inputs(numbers) from user. Divide the greater
number by the smaller number. Validate the user inputs, it should be integer type
only . If the input is not integer, raise exception and catch it. Also, if divisor is 0, catch
the exception raised.'''

def two_nos():
    try:
        x=int(input("Enter 1st num: "))
        y=int(input("Enter 2nd num: "))
        mx=max(x,y)
        mn=min(x,y)
        ans=mx/mn
    except ValueError as e:
        print("input should be integer type only....")
    except ZeroDivisionError as e:
        print("cannot divide anything by zero")
    else:
        print(ans)
#while 1:
two_nos()