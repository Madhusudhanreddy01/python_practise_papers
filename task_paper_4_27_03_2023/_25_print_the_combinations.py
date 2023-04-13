''' 25. Define a logic to print the combinations from the two the below input data Input :
 
 			'Department“. ['Bakkt’, 'Cisco'],
 			’Team’	: [’Red’, ’Yellow’, ’Black’]
Output :
 		{ ’Department“. ‘Bakkt’, ’Team“. ’Red’},
 		{ ’Department“. ‘Bakkt’, 'Team“. ’Yellow’}
 		{ ’Department“. ‘Bakkt’, 'Team“. ’Black’}
 		{ ’Department“. ‘Cisco’, ’Team“. ’Red’}
 		{ ’Department“. ‘Cisco’, ’Team“. ’Black’}
 		{ ’Department“. ‘Cisco’, ’Team': ’Yellow’}'''

input_data = {
   'Department': ['Bakkt', 'Cisco'],
   'Team': ['Red', 'Yellow', 'Black']
}

for i in input_data['Department']:
   for j in input_data['Team']:
       combination = {'Department': i, 'Team': j}
       print(combination)
