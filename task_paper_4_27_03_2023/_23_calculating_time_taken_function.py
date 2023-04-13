'''23. Write a logic for calculating the time taken for executing the python function'''

import time

start_time = time.time()
def add_(a,b):
   return a+b

print(add_(2,3))
print(add_(2,4))
print(add_(2,5))
print(add_(2,6))
print(add_(2,7))

end_time = time.time()

total_time = end_time - start_time
print(total_time)