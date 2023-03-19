'''26. You are given a string S. Your task is to find the indices of the start and end of string k in 
S 
The first line contains the string S.The second line contains the string k. 
Print the tuple in this format: (start _index, end _index). 
If no match is found, print (-1, -1).
                                                    
Sample Input 
Sample Output 
aaadaa 
aa 
(0, 1) 
(1, 2) 
(4, 5) '''

s = input()  # read string s from input
k = input()  # read string k from input

start_index = s.find(k)  # find the start index of k in s
end_index = start_index + len(k) - 1  # calculate the end index of k

if start_index == -1:  # if k is not found in s
    print((-1, -1))
else:  # if k is found in s
    print((start_index, end_index))
