'''10. In the given String -- ‘MsYs TecHNOlogiEs iS a gREat place To woRk’ 
find the count of  lowercase and uppercase letters. '''

String_="MsYs TecHNOlogiEs iS a gREat place To woRk"
lower_count=0 
upper_count=0

for i in String_:
    if(i.islower()):
        lower_count+=1
    if(i.isupper()):
        upper_count+=1
print(lower_count,upper_count)