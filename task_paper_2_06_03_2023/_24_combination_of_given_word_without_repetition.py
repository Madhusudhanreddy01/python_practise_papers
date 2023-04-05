# 24. You have given a string str1 = "abcbaefabcabchijkl" 
# your task is to find the combination of given word without repetition, present in the string , given  word 'abc' 
# o/p = 7 
# explanation : 
# abc, cba, 
# cba, 
# bca, acb 
# cab, bac 

def combinatin_word(String,word):  
    count=0
    for i in range(len(String)):
        new_word=String[i:i+len(word)]
        t=0
        for j in range(len(new_word)):
            if word[j] in new_word:
                t+=1
            if t==len(word):
                print(new_word)
                count+=1
    return count
        
string="abcbaefabcabcdhijkl"
word="abc"
print(combinatin_word(string,word))