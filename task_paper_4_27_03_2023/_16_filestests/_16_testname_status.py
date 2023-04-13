'''16. Let’s consider there are two files, one file contains testnames, 
other file contains testnames and status for each one. Generate a dictionary 
with key’s as testname and value as status.
Input : 
    FiIe1.txt: 
test1 
test2
    File2.txt: 
test1-pass 
test2-fail'''


# Output : { "test1" : "pass", "test2" : "fail"}


with open("File1.txt", "r") as file1:
    text1=file1.readline().split()
    print(text1)

dict_={}
with open('File2.txt', "r") as file2:
    for i in file2:
        var_1, var_2=i.split("-")
        dict_[var_1]=var_2.strip()
    print(dict_)