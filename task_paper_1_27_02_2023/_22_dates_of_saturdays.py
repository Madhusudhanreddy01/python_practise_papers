'''22. Write a function where month and year are taken as arguments which returns the 
output with all the dates of saturdays occuring the month'''

import calendar

def get_saturdays_in_month(month, year):
    saturdays = []
    for day in range(1, calendar.monthrange(year, month)[1]+1):
        if calendar.weekday(year, month, day) == calendar.SATURDAY:
            saturdays.append(day)
    return saturdays
print(get_saturdays_in_month(5,2023))