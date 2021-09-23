# Add full menu
# Entrees, Sides, Wine and Desserts

import random as r


#def menu():
 #   print()["[1]Entrees", "[2]Sides", "[3]Wines", "[4]Desserts, [0] Quit"]
  #  menu()


option = int(input(""))
while option != 0:
    if option == 1:
        chicken = r.randint(1, 6)
        beef = r.randint(1, 6)
        vegetarian = r.randint(1, 6)
        print(chicken, beef, vegetarian)

    elif option == 2:
        soup = r.randint(5, 10)
        salad = r.randint(5, 10)

    elif option == 3:
        merlot = r.randint(2, 5)
        chardonnay = r.randint(2, 5)
        pinot_noir = r.randint(2, 5)
        rose = r.randint(2, 5)

    elif option == 4:
        flan = r.randint(1, 3)
        creme_brulee = r.randint(1, 3)
        chocolate_moose = r.randint(1, 3)
        cheesecake = r.randint(1, 3)


