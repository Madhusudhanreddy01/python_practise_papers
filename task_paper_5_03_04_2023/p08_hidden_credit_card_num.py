'''8. Write a function in Python that accepts a credit card number. It should return a
string where all the characters are hidden with an asterisk except the last four.'''

def credit_card(n):
    res = ""
    l = len(n)
    for i in range(l):
        if i < l-4 :
            res += "*"
        else:
            res += n[i]
    return res

print(credit_card("1234567890120105"))

print("-----------or---------------")

def credit_card(cc_num):
    marked='*'*(len(cc_num)-4)+cc_num[-4:]
    return marked
cc_num='1234567890120105'
marked_num= credit_card(cc_num)
print(marked_num)