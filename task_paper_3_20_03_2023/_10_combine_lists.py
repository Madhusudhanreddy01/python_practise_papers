'''10. Write a function combine_lists should take two lists and return a new list
containing all elements from both lists.'''


def combine_lists(list1, list2):
    merge_list=list1+list2
    return merge_list

list1=[1,2,3,4]
list2=[4,5,6,7]
merge_list=combine_lists(list1, list2)
print(merge_list)