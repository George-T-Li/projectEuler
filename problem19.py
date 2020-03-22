# Counting Sundays

"""
Jan 1 1900 was a Monday
Months with 30 days: 4, 6, 9, 11
Months with 31 days: 1, 3, 5, 7, 8, 10, 12
Feb has 28 days, excpet for years divisible by 4, except for years divisible by 100, except for years divisible by 400
"""
# How many Sundays were on the first of a month, in the 20th century (Jan 1 1901 to Dec 31 2000)
# Jan 1 1901 was a Tuesday


def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        if year % 4 != 0:
            return 28
        else:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29

count = 0
daysSoFar = 365
month = 1
year = 1901

while year < 2001:
    numDays = days_in_month(month, year)
    daysSoFar += numDays
    if daysSoFar % 7 == 6:
        count += 1
    month += 1
    if month == 13:
        month = 1
        year += 1
print(count)
