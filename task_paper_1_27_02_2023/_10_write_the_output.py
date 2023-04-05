# 10. Write the output of the program: 
# match = ‘version’, input=’Upgraded_image_version_8.0.4.3’ 
# if match in input: 
# print(‘YES’) 
# else: 
# print(‘NO’)

import re

match = 'madhu'

input1 ='Upgraded_image_version_8.0.4.3'

x = re.findall(match,input1)
if str(*x) == match:
    print("Yes")
else:
    print("No")

#-----------------------------------------------------------
 
# match = "version"
# input="Upgraded_image_version_8.0.4.3"
# if match in input: 
#     print("YES") 
# else: 
#     print("NO")


# -------------------------------------------------

# import re
# s="Upgraded_image_version_8.0.4.3"
# pattern="madhu"
# for m in re.findall(pattern,s):
#     print(type(m))
#     if m in s:
#         print("Yes")
#         break
# else:
#     print("No")

# -------------------------------------------------------------------

# input1=input("enter the string and special characters\n")
# input1=repr(input1)
# match=input("enter the string and special characters\n")
# match=repr(match)

# import re
# x=re.findall(input1, match)
# print("Yes" if str(*x) in match else "No")

