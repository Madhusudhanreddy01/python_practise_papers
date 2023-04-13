'''7. In the given string, remove the special characters and add a space instead of 
that “Msys&Technologies@Chennai'''

string_= "Msys&Technologies@Chennai"
res_=""
for i in string_:
    if i in "!@#$%^&*":
        res_ += ""
    else:
        res_ += i

print(res_)