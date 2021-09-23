# add roles, Waiter, Customer or Manager
import fullmenu as fm
def roles():
    print()["[6] Waiter", "[7]Customer", "[m] Manager", "[0] Quit"]
    roles()


option = int(input(""))
while option != 0:
    if option == 6:
        print("This is we have avalable", fm.chicken, fm.beef, fm.vegetarian)

    elif option == 7:
        print("Hello")
