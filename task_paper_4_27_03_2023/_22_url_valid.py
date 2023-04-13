'''22. Define the logic for verifying whether URL is Valid or Invalid Requirements for Valid URL
• Should not contain any Special characters [,*,&,%,$,#,@,!] and Spaces
• Should start with https://
Input : URLs will be stored inside a file , read the URLs from the input file [input.txt]
Output : Generate a .txt file which contains the information whether URL is valid or not ( URL, Status [valid/invalid])
Example:
Input
Input.txt [text file]
https://m 
http s://m
Output:
1. https://m, valid
2. http s://m, invalid
 
Note: Define the logic with different approaches [1. Using RegEx 2. Without RegEx]
'''

pattern = r"^https://[\w \s.]*$"
with open("input1.txt","r") as file1:
   urls = file1.read().splitlines()
with open("output1.txt","w") as file2:
   for i ,url in enumerate(urls):
       if re.match(pattern,url):
           file2.write(f"{i+1}.{url} valid\n")
           print(f"{url} valid")
       else:
           file2.write(f"{i+1}.{url} invalid")
           print(f"{url} invalid")