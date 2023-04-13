'''3. Write Python Program to delete element from array at given index.'''

list_=[1,2,3,4,5,6,7,8]
index=int(input("Enter Index Position: "))

delete=list_[:index]+list_[index+1:]
print(delete)
print("Deleted value is : ", index+1)
