'''30. Convert each list element to a key-value pair.
ex:
Input : test_list = [2323, 82, 129388, 95]
Output : {23: 23, 8: 2, 129: 388, 9: 5}'''

test_list = [2323, 82, 129388, 234, 95]
print("The original list is : " + str(test_list))
res = dict()
for ele in test_list:
    mid_idx = len(str(ele)) // 2
    key = int(str(ele)[:mid_idx])
    val = int(str(ele)[mid_idx:])
    res[key] = val
print("Constructed Dictionary : " + str(res))