'''28. Standardize mobile numbers when given N mobile numbers. Sort them in
ascending order. Print them in the standard format.'''

def Standardize_mobile_number(*mob_nums):
    res = []
    for mob_num in mob_nums:
        mob_num = sorted(mob_num, reverse=True)
        # mob_num.insert(0,mob_num.pop())
        mob_num = "".join(mob_num)
        res.append(f"+91 {mob_num}")
    return res

mob_nums = [num for num in input('Enter the mobile numbers : ').split()]

print(Standardize_mobile_number(*mob_nums))