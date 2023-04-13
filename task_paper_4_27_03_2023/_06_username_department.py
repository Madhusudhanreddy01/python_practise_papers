'''6. Define the logic for generating the email id based on username and department Get the username and department as a input and create a email id from it
input : username : msys 
department: automation
Output: msys.automation@gmail.com'''

def generate_email(username,department):
    email_prefix= username.lower()+ '.' +department.lower()+'@'+'gmail.com'
    return email_prefix
username='msys'
department='automation'
print(generate_email(username,department))