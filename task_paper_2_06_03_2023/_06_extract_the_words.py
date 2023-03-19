# 6. Write a program to extract the words starting with lowercase letters 
# present in the list. [‘Nissan’,  ‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’]

# Define the list of words
my_list = ['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']

# Extract the words starting with lowercase letter
lowercase_words = [word for word in my_list if word[0].islower()]

# Print the extracted words
print(lowercase_words)
