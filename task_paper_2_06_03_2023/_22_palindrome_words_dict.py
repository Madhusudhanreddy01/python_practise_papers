'''22. Find the palindrome words with the count value from the given string.Output should be in the form of dict. key will be a palindrome word and value will be number of occurence. 
i/p given a string - Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331.  
o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2} '''


a="Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis If we reverse the number 1331 then we also get 1331" 
b=a.split(" ")
list_=[]
for i in range(len(b)):
    c=(b[i][::-1]).upper()
    d=b[i].upper()
    if (c==d):
        if(len(d)!=1):
            list_.append(d)
set_=sorted(list(set(list_)))
dict_={}
for i in set_:
    dict_[i]=(list_.count(i))
print(dict_)