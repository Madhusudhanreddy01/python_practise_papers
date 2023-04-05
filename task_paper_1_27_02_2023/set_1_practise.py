import time
from threading import *
print(current_thread().getName())
def first_Thread():
   print ("First Child Thread Running")
   time.sleep(1)
print ("First Child Thread Done")
def Second_Thread():
    print ("Second Child Thread Running")
    time.sleep(1)
print ("Second Child Thread Done")
Thread(target=first_Thread).start()
Thread(target=Second_Thread).start()