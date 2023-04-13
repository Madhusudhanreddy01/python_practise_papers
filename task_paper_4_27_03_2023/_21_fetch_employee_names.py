'''21.Imagine a scenario where you are required to fetch the employee names who joined after 02 Sep 2022 and location is Hyderabad 
empIoyee_ data = { 
“priya”:{“location”: “Hyderabad” “joining_date” :“05/09/2022” },
  “mahi”: {“location”: “Bangalore” “joining_date”: “20/02/2023”}, 
  “raja”: {“location”    : “Hyderabad”, “joining_date” : “14/10/2022”},
 “prabhu”:{“location”: “Bangalore” “joining_date” : “02/01/2023”}
 }
'''

employee_data = {
   "priya": {"location": "Hyderabad", "joining_date": "05/09/2022"},
   "mahi": {"location": "Bangalore", "joining_date": "20/02/2023"},
   "raja": {"location": "Hyderabad", "joining_date": "14/10/2022"},
   "prabhu": {"location": "Bangalore", "joining_date": "02/01/2023"}
}


for employee_name, employee_info in employee_data.items():
   # print(employee_name)
   # print(employee_info)
   if employee_info["location"] == "Hyderabad" and employee_info["joining_date"] > "02/09/2022":
       print(employee_name)
