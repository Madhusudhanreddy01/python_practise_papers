# 8. Write Row class that accepts any keyword arguments given to it and stores these
# arguments as attributes.
# Ex. >>> row = Row(a=1, b=2)
# >>> row.a
# 1
# >>> row.b
# 2

class Row:
    def __init__(self, **args):
        self.__dict__.update(args)

row = Row(a=1, b=2, c=3, d=4)
print(row.a)
print(row.b)
print(row.d)