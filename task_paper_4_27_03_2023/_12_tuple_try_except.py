'''12. Solve the following scenarios
• Let’s assume that there is a tuple containing username, You have got a requirement to add password also into it.
o Input : (“user1”)
o Output : (“user1”,”password1”)
• Below logic is failing with an error message, Instead of auto generated Error, Please display the user defined message saying “Error : Cannot concatenate String and Number”
print(“msys” + 2007)'''


t=("usernasme",)
l=t+("password",)
print(l)
try:
    username = "user"
    password = 1234
    login_info = (username, password)
    login_info = login_info[0] + "," + str(login_info[1])
    login_info("user"+1234)
    # do something with the login_info tuple
except TypeError:
    print("error: cannot concatenate string and number")