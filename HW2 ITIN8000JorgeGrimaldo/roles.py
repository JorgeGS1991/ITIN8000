# add roles, Waiter, Customer or Manager
import fullmenu as fm
# Will check if its a Customer, Waiter or Manager
# c for Customer, w for Waiter and m for manager
def getroles(Cinput):
    if Cinput == "c":
        print("Please Make a Selection from the Menu")
        fm.prtMenuList("*", "c")
        return ""
    elif Cinput == "w":
        fm.prtMenuList("*", "w")
        return ""
    else:
        # This is for debugging purpose
        return ""






