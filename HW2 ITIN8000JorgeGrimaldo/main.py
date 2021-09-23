#The project should simulate the operation of a restaurant.
# When I run main.py it should start by randomly generating a quantity for each of the menu items in the restaurant.
# These quantities will have to go down when customers order the menu items.
# Each customer order can contain an Entree, Side, Wine, and a Dessert.

import fullmenu as m

menu = m.random()
print(menu)

def menu():
    print("FullMenu")
    print("[2] Option 2")
    print("[0] Exit the program")

menu()
option = int(input("Enter your Option"))

while option != 0:
    if option == 1:
        print()

    elif option == 2:
        print("Print option 2")

    else:
        print("invalid option")

    menu()
    option = int(input("Enter your option"))

