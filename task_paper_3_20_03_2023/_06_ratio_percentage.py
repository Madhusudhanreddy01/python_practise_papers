# 6. Write a function to_percent which accepts a number representing a ratio and
# returns a string representing the percentage representation of the number to one
# decimal place.


def ratio_percentage(a):
    num = a.split(":")
    res = round(int(num[0])/int(num[1]) * 100, 2)
    return res
print(ratio_percentage("1:2"))