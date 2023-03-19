'''11. Write a python function with the name reverse_vowel that takes one string as an 
argument and  reverse the order of vowels present in the string. 
The function should return the string having  reversed order of vowels. 
For example – If the input string which is given as an argument is ‘Hello’  
then the output string should be ‘Holle’. You need to reverse the vowel 
irrespective of lowercase or  uppercase. '''

word="hello"
str_=""
vowel_catch=""
for i in (word):
    if(i in ["a","e","i","o","u"]):
        str_+="_"
        vowel_catch+=i
    else:
        str_=str_+i
rev_vowel_orde=(list(reversed(sorted(vowel_catch))))
count=-1
result=""
for i in str_:
    if(i=="_"):
        count=count+1
        result+=(rev_vowel_orde[count])

    else:
       result+=i
# print(rev_vowel_orde)
print(result)