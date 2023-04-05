# 9. Create a function is_leap_year that accepts a year and returns True if (and only
# if) the given year is a leap year.

def checkyear(year):
    if (year%4)==0:
        if (year%100)==0:
            if (year%400)==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year=2024
print(checkyear(year))