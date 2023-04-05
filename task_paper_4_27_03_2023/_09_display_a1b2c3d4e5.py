# 9. Given a string “abcde”, Display the output as “a1b2c3d4e5”

def add_indexes(s):
    output_str=""
    for i,c in enumerate(s):
        output_str += c + str(i+1)
    return output_str
s="abcde"
print(add_indexes(s))