'''5. Can we order a dictionary? How? 
We can sort lists, tuples, strings, and other iterable objects in python since they are all ordered objects. Well, as of python 3.7, dictionaries remember the order of items inserted as well. Thus we are also able to sort dictionaries using python’s built-in sorted() function. Just like with other iterables, we can sort dictionaries based on different criteria depending on the key argument of the sorted() function.

sorted() function
The sorted() function can accept three parameters: the iterable, the key, and reverse.

sorted(iterable, key, reverse)

In contrast to the sort() method which only works on lists, the sorted() function can work on any iterable, such as lists, tuples, dictionaries, and others. 
However, unlike the sort() method which returns None and modifies the original list, 
the sorted() function returns a new list while leaving the original object unchanged.

Note: No matter what iterable is passed in to the sorted() function, it always returns a list.

Sorting a Dictionary
Dictionaries are made up of key: value pairs. Thus, they can be sorted by the keys or by the values.

Let’s say that we have a dictionary, with the keys being names, and the values being ages.

dictionary_of_names = {'beth': 37, 
                       'jane': 32,
                       'john': 41, 
                       'mike': 59
}
If we just pass in the entire dictionary as the iterable to the sorted() function, we will get the following 
output:

print(sorted(dictionary_of_names))
# ['beth', 'jane', 'john', 'mike']
As we can see, if we pass in the entire dictionary as the iterable to the sorted() function, 
it returns a list that contains only the keys sorted alphabetically.

OrderedDict is a subclass of dictionary which remembers the order of entries added in a dictionary object. 
When iterating over an ordered dictionary, the items are returned in the order their keys were first added.

>>> from collections import OrderedDict
>>> D = {5:'fff', 3:'ttt', 1:'ooo',4:'bbb', 2:'ddd'}
>>> OrderedDict(D.items())
 OrderedDict([(5, 'fff'), (3, 'ttt'), (1, 'ooo'), (4, 'bbb'), (2, 'ddd')])

We also need to use a sorted() function that sorts elements in an iterable in a specified order. 
The function takes a function as an argument which is used as a key for sorting. Since we intend to sort dictionary on values, 
We take the 1st element of the tuple as key for sorting.

>>> OrderedDict(sorted(D.items(), key=lambda t: t[1]))
   OrderedDict([(4, 'bbb'), (2, 'ddd'), (5, 'fff'), (1, 'ooo'), (3, 'ttt')])
The OrderedDict object can be parsed into a regular dictionary object

>>> D1 = dict(OrderedDict(sorted(D.items(), key = lambda t: t[1])))
>>> D1
   {4: 'bbb', 2: 'ddd', 5: 'fff', 1: 'ooo', 3: 'ttt'}'''






my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}
print(sorted_dict)
# Output: {'a': 1, 'b': 2, 'c': 3}
