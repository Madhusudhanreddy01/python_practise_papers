'''11.Define Calculator logic in such a way that addition and subtraction functions should be 
in one python file and multiplication and division should be in another python file, 
Access these functions and utilize them inside the main file.'''

from _11_add_subtract import add, subtract
from _11_multi_divide import multi, divide

result = add(3,4)
print(result)

s=subtract(4,3)
print(s)

result=multi(3,4)
print(result)

d=divide(3,4)
print(d)