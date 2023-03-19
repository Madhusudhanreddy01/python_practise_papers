# 23. Find the highest sum of the string by removing the duplicates for each 
# iteration input=’1211’

input_="12221133"
c=" ".join(input_).split(" ")
a=0
store=[]
while a<len(c):
    acess=sum(set(list(map(int,c[a:]))))
    store.append(acess)
    a=a+1
print(max(store))

# -----------------------------
string = input("Enter the string : ")

unique_elements = set([int(i) for i in string])

print(sum(unique_elements))
