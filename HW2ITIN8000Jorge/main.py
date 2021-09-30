# The project should simulate the operation of a restaurant.
# When I run main.py it should start by randomly generating a quantity for each of the menu items in the restaurant.
# These quantities will have to go down when customers order the menu items.
# Each customer order can contain an Entree, Side, Wine, and a Dessert.
# import roles as ro
import fullmenu as fm
import roles as ro
import random as r

# Re-open Restaurant
rOpne = False
run = True
fm.initAllLists()

while run:
    if rOpne == False:
        print("Restaurant is Closed, Come back tomorrow")
        Cinput = input(" If you are a Manager use M to Open the Restaurant\n ").upper()

        if Cinput == "M":
            fm.initAllLists()
            mrt = ro.getroles("w")
            rOpne = True
            print(mrt)
        else:
            print(Cinput + " is not a valid Option")

    else:
        print("Welcome to the UNO restaurant ")
        Cinput = input(" Choose: \n w for Waiter \n c for Customer \n m for Manager \n ").lower()
        print()
        # if exit is false program will end
        if Cinput == "exit":
            run = False
        else:
            # print("get Roles")
            urt = ro.getroles(Cinput)
            print(urt)
            # fix if so it doesn't update count when W is selected.
            # Check if the customer did not enter a valid option
            vop = True
            if Cinput == "c":
                while vop:
                    print("---------------------------")
                    CustInput = input(
                        "Make your code selection, use a comma to separate your selection \n EXP: \n E1,W1 \n or "
                        " R for Random Order ")
                    orList = list(CustInput.split(","))
                    nItemError = False
                    # check if any aren't available

                    err = False
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

                        elif ckSel == "R":
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
                                        print("")
                            print("You Have selected a Random Order \n "

                                  "\n" + fm.rDl, "\n" + fm.rEl,
                                  "\n" + fm.rSl, "\n" + "and", fm.rWl +
                                  "\n \nIf You are not Happy with Your Order"
                                  "\nYou can make a different Selection \n"

                                  "----------------------------------------")


                        #             print("Your Random Order is: \n", fm.item)

                        else:
                            # Return to ask for a correct code
                            print("---------------------------")
                            print("Invalid input!  " + ckitems + "\n")
                            err = True
                    if not err:
                        vop = False

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
                    rOpne = False
                    fm.clrAllLists()
                    print(fm.rclosed())
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
