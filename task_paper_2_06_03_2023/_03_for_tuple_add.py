'''3. Given a tuple (“Msys”, “Technologies”, “2007”), add “Python” at the end of this 
tuple and the  output should also be in the form of tuple. 
Make a note that tuples are immutable in nature so you  need to find some idea to make 
modifications and print the updated tuple.'''


t = ("Msys", "Technologies", "2007")
t1 = ("Python",)
print(t+t1)


t2 = ("Msys", "Technologies", "2007")
t3 = ["Python"]
t4 = list(t2)
t4.extend(t3)
print(t4)

s =("Msys", "Technologies", "2007")
s1 = list(s)
s1.append('python')
print(s1)