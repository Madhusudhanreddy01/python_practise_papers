'''4. Define a function which returns dictionary that stores the words and it’s length from the given text
text = “Be happy”
Expected Output : {“Be'.2,”happy”:5}'''

def word_length(text):
    words=text.split()
    word_dict={}
    for word in words:
        word_dict[word]=len(word)
    return word_dict
s='I am Madhusudhan'
print(word_length(s))