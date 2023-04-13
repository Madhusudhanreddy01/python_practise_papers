'''5. Let’s consider there is a list which contains usernames, You have received requirement to add one more username to the list (without using append and assignment approaches) 
input : [“user1”,”user2”]
output : [“user1”,”user2”,”user3”]'''

usernames=['user1','user2']
new_user='user3'
usernames=usernames+[new_user]
print(usernames)