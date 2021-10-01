# Ask for the users first and last name, favorite color, and date of birth
# Calculate how many days old the user is
# Write the user's name in the format last name, first name and favorite color in a .txt named UserName
# Write the user's age in days to a binary file named Days Old
# Add the user to a CSV file named UserData.csv in the order Last Name, First Name, Favorite Color, Days Old

from datetime import date
import pandas as pd


# Ask for the users first and last name, favorite color, and date of birth
UfName = input(" What's your Fist Name: ")
UlName = input(" What's your Last Name: ")
UfColor = input(" What's your Favorite Color? ")

# Ask user for birthday information
bd_m = int(input(" What MONTH (MM) were you born: "))
bd_d = int(input(" What DAY (DD) were you born: "))
bd_y = int(input(" What YEAR (YYYY) were you born: "))

# Transfer Fname, LName and FColor to UserName.txt file
with open('UserName.txt', 'w') as f:
    f.write('{} {} {}'.format(UlName, UfName, UfColor))


# Calculate user's days old
def calculateAge(birthDate):
    age = int((date.today() - birthDate).days)
    return age


days = calculateAge(date(bd_y, bd_m, bd_d))

# print(days, "Days Old")
# Days old to Binary
dOld = format(int(days), 'b')

# Transfer user's age in days to a binary file "DaysOld"
with open('DaysOld', 'w') as d:
    d.write('{}'.format(dOld))

# Add the user to a CSV file named UserData.csv
# in the order Last Name, First Name, Favorite Color, Days Old
data = {
    'Last Name': [UlName],
    'First Name': [UfName],
    'Favorite Color': [UfColor],
    'Days Old': [dOld]
}

df = pd.DataFrame(data)
df.to_csv("UserData.csv")

print("\n\n Thank you for Participating")
