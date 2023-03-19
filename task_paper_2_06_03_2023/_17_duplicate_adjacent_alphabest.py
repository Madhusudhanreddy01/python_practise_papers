'''17. Write a program to replace duplicate adjacent alphabets from a given string with ‘_’. 
For Example -- input given string : 'abcdaa hssbbye' and output : ‘abcda_ hs_b_ye’ '''

string ='abcdaa hssbbye' 
str_=""
for i in range(len(string)-1):
    if(string[i]!=string[i+1]):
      str_=str_+string[i]
    if(string[i]==string[i-1]):
        str_=str_+"_"
 
print(str_)