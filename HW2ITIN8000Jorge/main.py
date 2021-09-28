# The project should simulate the operation of a restaurant.
# When I run main.py it should start by randomly generating a quantity for each of the menu items in the restaurant.
# These quantities will have to go down when customers order the menu items.
# Each customer order can contain an Entree, Side, Wine, and a Dessert.
# import roles as r
import fullmenu as fm
import roles as ro

run = True
fm.initAllLists()

while run:
    print("Welcome to the UNO restaurant ")
    Cinput = input(" Choose: \n w for Waiter \n c for Customer \n m for Manager \n ").lower()
    print()
    if Cinput == "exit":
        run = False
    else:
        # print("get Roles")
        urt = ro.getroles(Cinput)
        print(urt)
        # fix if so it doesn't update count when W is selected.
        if Cinput == "c":
            CustInput = input("Make your code selection, use a comma to separate your selection \n EXP: \n E1,W1 \n ")
            orList = list(CustInput.split(","))
            nItemError = False
            # check if any aren't available
            for ckitems in orList[0:]:
                ckSel = ckitems[0:1]
                if ckSel == "W":
                    if fm.getWineList(ckitems):
                        print("Wine " + ckitems + " is not available, make another selection")
                        nItemError = True
                elif ckSel == "D":
                    if fm.getDessertList(ckitems):
                        print("Dessert " + ckitems + " is not available, make another selection")
                        nItemError = True
                elif ckSel == "S":
                    if fm.getSidesList(ckitems):
                        print("Side " + ckitems + " is not available, make another selection")
                        nItemError = True
                elif ckSel == "E":
                    # print("Selection E")
                    if fm.getEntreeList(ckitems):
                        print("Entree " + ckitems + " is not available, make another selection")
                        nItemError = True
                else:
                    #Return to ask for a correct code
                                        print("")



            # Update each entry
            if nItemError == False:
                for items in orList[0:]:
                    mnSel = items[0:1]
                    if mnSel == "W":
                        fm.updWineList(items)
                    elif mnSel == "D":
                        fm.updDessertList(items)
                    elif mnSel == "S":
                        fm.updSidesList(items)
                    elif mnSel == "E":
                        fm.updEntreeList(items)
                    else:
                        urt = ro.getroles(Cinput)
                        print("Invalid Selection ")
        elif Cinput == "m":
            print("---------------------------")
            print("Manager Menu")
            print("---------------------------")
            mgrInput = input('Make a selection, \n C = Closed Restaurant \n or \n N = Re-Open Restaurant ')
            if mgrInput == "C":
                print("Restaurant is Closed and Food is not available")
                fm.clrAllLists()
                fm.prtMenuList("*", "w")
            elif mgrInput == "N":
                fm.initAllLists()
                mrt = ro.getroles("w")
                print(mrt)
        elif Cinput == "w":
            print("---------------------------")
            print("Waiter Menu")
            print("---------------------------")

        else:
            print("Invalid Option, try again")
            print()
