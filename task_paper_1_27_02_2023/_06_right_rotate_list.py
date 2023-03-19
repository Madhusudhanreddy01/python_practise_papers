'''6. Write a python program to right rotate a List by n 
Enter position to rotate list item: 3 
Sample input: [10, 20, 30, 40, 50, 60, 70] 
Expected output: [50, 60, 70, 10, 20, 30, 40]'''

# Normal
n=[10, 20, 30, 40, 50, 60, 70]

pos_=int(input())

res_=n[-pos_:]+n[:-pos_]
print(res_)

# ----------------------------------------------
#Functions
def right_(n):
    pos_=int(input())

    res_=n[-pos_:]+n[:-pos_]
    print(res_)
n=[10, 20, 30, 40, 50, 60, 70] 
right_(n)
