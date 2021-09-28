
""""This is my code for homewoork 1 """
# import datatime
from datetime import datetime

# ask user to type username
username = input("Whats your name ")

# get the lines stap fro today
today = datetime.now()
# Get months name from todays date
month_name = today.strftime("%B")


# Extract the day of the month as a number from today's date
day_number = today.day

# if the day is equals to 1, 21 or 31 the suffix will be st
if day_number == 1 or day_number == 21 or day_number == 31:
    suffix = "st"
# if the day is equals to 2 or 22 the suffix will be nd
elif day_number == 2 or day_number == 22:
    suffix = "nd"
# if the day is equals to 3 or 23 the suffix will be rd
elif day_number == 3 or day_number == 23:
    suffix = "rd"
# else the suffix will be th
else:
    suffix = "th"

#extract the year as a number from today's date
year_number = today.year

# if day_number == 0, then its an "even" number
if day_number% 2 == 0:
    day_type = "even"
# else the number is "odd"
else:
    day_type = "odd"

# Print out the Statement including month_name, day_number, year_number, today.month*day)number and day_type.
print("Hello.", username, "Todays Date is", month_name, str(day_number) + suffix, "of", str(year_number),
      "The product of the month and day is", today.month * day_number, "which is an", day_type, "number.")


#Loop
#Define n-1
n = 1
#While  n <= day_number
while n <= day_number:
    print(n)
# n = n + 1
    n = n + 1
#End Loop

#Print days
print("days")
print ("If you counted the days this month so far you would have",str(n -1) + suffix,"days.")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/