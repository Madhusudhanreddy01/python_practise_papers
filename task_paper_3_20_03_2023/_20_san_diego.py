'''20. Create a function that determines which day of the month the San Diego Python
meetup should be. It should accept year and month arguments and should return
a datetime.date object representing the day of the month for the meetup.
>>> meetup_date(2012, 3)
datetime.date(2012, 3, 22)'''


import datetime

def meetup_date(year,month):
   first_day = datetime.date(year,month,1)
   first_meetup_day = (meetup_day - first_day.weekday())%7+1
   meetup_date = datetime.date(year,month,first_meetup_day) + datetime.timedelta(weeks = meetup_week-1)
   return meetup_date

#meetup_day --> monday = 0 ,tuesday = 1 ,wednesday = 2 ,thursday = 3 ,friday = 4 ,saturday = 5 ,sunday = 6
meetup_day = int(input("enter the meetup_day : "))
#(1 to 5) --> week
meetup_week = int(input("enter the meetup_week : "))
print(meetup_date(2023,3))