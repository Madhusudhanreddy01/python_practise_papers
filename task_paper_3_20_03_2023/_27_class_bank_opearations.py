# '''27. Write a class that represents a bank account, do bank operations.'''

# class Bank_Account:
#     bank_name = 'HDFC BANK'
#     branch = 'BENGALURU'
#     ifsc_code = 'HDFC0004341'

#     def __init__(self,Acc_name,Acc_no,ifsc,balance):
#         self.Acc_Name = Acc_name
#         self.Acc_No = Acc_no
#         self.IFSC = ifsc
#         self.Balance = balance

#     def account_details(self):
#         pass

#     def __str__(self):
#         return f''' ==== Account Details =======
#         Bank Name: {self.bank_name}
#         branch: {self.branch}
#         ifsc: {self.ifsc_code}'''
   
#     def deposit(self,amount):
#         self.Balance += amount
#         print(f"the amount of {amount} is deposited successfully.current balance is {self.Balance}")

#     def withdraw(self,amount):
#         if amount > self.Balance:
#             print("the amount is insufficient")
#         else:
#             self.Balance -= amount
#             print('withdrawal of {amount} is successful and current balance is {self.Balance}')

#     def get_balance(self):
#         return self.Balance

# deposit = int(input("Enter deposit amount: "))
# withdraw = int(input("Enter withdraw amount: "))
# customer_1 = Bank_Account('Madhusudhan',50100366141772,'HDFC0004341 ',5000)
# print(customer_1.Acc_Name)
# customer_1.deposit(deposit)
# customer_1.withdraw(withdraw)
# print(customer_1.get_balance())
# print(customer_1)

print("----------------------------Another-------------------------------")

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
