'''5. Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’,  
‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values 
associated  with keys in alphabetically sorted order.'''

d ={'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'}
print(d)

print("----------------")

k = sorted(d.items(), key=lambda x : x[1] )
print(dict(k))

print("----------------")

k = sorted(d.items())
print(dict (k))