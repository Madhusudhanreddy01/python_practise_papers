'''18. Create your own exception.'''

try:
    a=int(input("Enter:"))
    b=input("Enter num:")

    if a > b:
        print("True")
    else:
        raise TypeError
except TypeError:
    print("Both values are not same datatype.")
          