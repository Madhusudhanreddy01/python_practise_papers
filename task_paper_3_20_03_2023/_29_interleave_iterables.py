'''29. Write a function called interleave which accepts two iterables of any type and
returns a new iterable with each of the given items "interleaved" (item 0 from
iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).
'''

def interleave(iterable1, iterable2):
   res_type = type(iterable1)
   res = []

   iter1 = iter2 = 0

   while iter1 < len(iterable1) and iter2 < len(iterable2):
       res += [iterable1[iter1]]
       iter1 += 1
       res += [(iterable2[iter2])]
       iter2 += 1

   if iter1 < len(iterable1):
       res += iterable1[iter1:]
   if iter2 < len(iterable2):
       res += iterable2[iter2:]

   return res

print(interleave([1, 2, 3], [4, 5, 6, 7]))