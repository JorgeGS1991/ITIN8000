# Ask for the users first and last name, favorite color, and date of birth
# Calculate how many days old the user is
# Write the user's name in the format last name, first name and favorite color in a .txt named UserName
# Write the user's age in days to a binary file named Days Old
# Add the user to a CSV file named UserData.csv in the order Last Name, First Name, Favorite Color, Days Old

from datetime import date

# Ask for the users first and last name, favorite color, and date of birth

UfName = input(" What's your Fist Name: ")
UlName = input(" What's your Last Name: ")
UfColor = input(" What's your Favorite Color? ")

# Calculate Days old
bd_m = int(input("What MONTH were you born: "))
bd_d = int(input("what DAY were you born: "))
bd_y = int(input("What YEAR were you born: "))

now = date.today()

age = date(int(bd_y), int(bd_m), int(bd_d))
print("Your age is ", now - age)
days = now - age


# Transfer Fname, LName and FColor to UserName.txt file
with open('UserName.txt', 'w') as f:
    f.write('{} {} {}'.format(UlName, UfName, UfColor))

# Transfer user's age in days to a binary file "DaysOld"
temp = format(days, 'b')

print(temp)

