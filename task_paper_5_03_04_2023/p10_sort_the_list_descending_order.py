'''10. Sort the list of integers in descending order without using inbuilt functions .
lst = [56,2,13,1,78,4,6]'''


lst = [56,2,13,1,78,4,6]
for i in range(len(lst)): 
    for j in range(i + 1, len(lst)): 
        if lst[i] > lst[j]: 
           lst[i], lst[j] = lst[j], lst[i] 
dec_ord_sort=lst[::-1]
print('decending order sort : ',dec_ord_sort)

print("------------or---------------------")

list_= [56,2,13,1,78,4,6]

for i in range(len(list_)-1,0,-1):
    for j in range(i):
        if list_[j] < list_[j+1]:
            list_[j],list_[j+1]=list_[j+1],list_[j]
print('decending order sort : ',list_)