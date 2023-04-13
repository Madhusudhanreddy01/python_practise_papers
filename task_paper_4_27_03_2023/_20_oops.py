 
'''20. Define sample code to achieve the following OOPs concepts
 
• Inheritance
• Method Overriding
• Encapsulation
• Method overloading
• Abstraction'''

print("-----------------------------------inheritance------------------------------------------")
#inheritance
class vehicle:
   def __init__(self,make,model,year):
       self.make = make
       self.model = model
       self.year = year

class car(vehicle):
   def __init__(self,make,model,year,car_wheels):
       super().__init__(make,model,year)
       self.car_wheels = car_wheels
   def started(self):
       print("car is ready to drive")

class bike(vehicle):
   def __init__(self,make,model,year,bike_wheels):
       super().__init__(make,model,year)
       self.bike_wheels = bike_wheels
   def started(self):
       print("bike is ready to drive")

a = car("skoda","rapid",2023,4)
b = bike("royal enfield","himalayan",2020,2)

print(a.make)
print(a.model)
print(b.model)
a.started()

print("-----------------------------------method overriding------------------------------------------")
#method overriding

class animal:
   def make_sound(self):
       print("generic animal sound")
class cat(animal):
   def make_sound(self):
       print("meow")

a = cat()
a.make_sound()

print("-----------------------------------method overloading------------------------------------------")

#method overloading

class add_method:
   def add(self,x,y):
       return x+y
   def add(self,x,y,z):
       return x+y+z

a = add_method()
print(a.add(2,3,4))

print("-----------------------------------encapsulation------------------------------------------")
#encapsulation

class hdfc_bank:
   def __init__(self,account_number,customer_name,balance = 0):
       self.account_number = account_number
       self.customer_name = customer_name
       self.balance = balance

   def deposit(self,amount):
       if amount > 0:
           self.balance += amount
       else:
           print("invalid deposit number")

   def withdraw(self,amount):
       if amount <= self.balance:
           self.balance -= amount
       else:
           print("insufficient balance")

   def get_balance(self):
       return self.balance

   def get_accountnumber(self):
       return self.account_number

   def get_customer_name(self):
       return self.customer_name

   def __str__(self):
       return f"Account Number: {self.__accountNumber}\nCustomer Name: {self.__customerName}\nBalance: {self.__balance}"


a = hdfc_bank("50100366141772","madhusudhan",1000)
print(a.balance)
print(a.customer_name)
a.deposit(1000)
print(a.balance)
a.withdraw(1997)
print(a.balance)

print("-----------------------------------abstraction------------------------------------------")
#abstraction

from abc import ABC,abstractmethod

class shape(ABC):
   def area(self):
       pass

class square(shape):
   def __init__(self,side):
       self.side = side

   def area(self):
       return self.side * self.side

a = square(5)
print(a.area())
