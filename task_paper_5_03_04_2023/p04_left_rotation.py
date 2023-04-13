'''4. Write Python program to perform left rotation of array elements by two positions.'''

#Left rotation
def rotate(pos1, pos2):
    return pos1[pos2:]+pos1[:pos2]

print(rotate([1,2,3,4,5,6], 2))

