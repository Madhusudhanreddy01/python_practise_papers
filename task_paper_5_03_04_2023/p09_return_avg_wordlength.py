'''9. For the given sentence, return the average word length. 
sentence = "I need to work very hard to learn more about algorithms in Python!" 
Note: Remember to remove punctuation first.'''

import string

sentence = "I need to work very hard to learn more about algorithms in Python!"
sentence = sentence.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
words = sentence.split()
total_length = sum(len(word) for word in words)
average_length = total_length / len(words)
print(average_length)