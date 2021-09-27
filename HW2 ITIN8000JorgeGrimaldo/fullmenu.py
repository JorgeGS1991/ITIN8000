# Add full menu
# Entrees, Sides, Wine and Desserts
import random as r

#import roles

#This is a list
#def menu():
lstEntrees = [["Chicken ", r.randint(1, 6), "E1"],
             ["Beef ", r.randint(1, 6), "E2"],
             ["vegetarian ", r.randint(1, 6), "E3"]]
lstSides = [["soup ", r.randint(5, 10), "S1"],
             ["salad ", r.randint(5, 10), "S2"]]
lstWines = [
             ["merlot ", r.randint(2, 5), "W1"],
             ["chardonnay ", r.randint(2, 5), "W2"],
             ["pinot ", r.randint(2, 5), "W3"],
             ["rose ", r.randint(2, 5), "W4"]]
lstDesserts = [
             ["flan ", r.randint(1, 3), "D1"],
             ["creme_brulee ", r.randint(1, 3), "D2"],
             ["chocolate_moose ", r.randint(1, 3), "D3"],
             ["cheesecake ", r.randint(1, 3), "D4"]
             ]
#This is for debugging purpose
"""    print("Avalable in Menu")
    for items in fmenuList[0:]:
        itemName = items[0]
        tot = items[1]
        print(itemName, tot)
        """
# Selection  parm is for *, e, s, d
#type par is for w,c
def prtMenuList(selction, type):
        if selction == "*":
            print("[Entrees]")
            for items in lstEntrees[0:]:
                itemName = items[0]
                tot = items[1]
                ocode = items[2]
                if type == "w":
                    print(" " + itemName, tot)
                else:
                    print(" " + itemName,ocode)

            print("[Sides]")
            for items in lstSides[0:]:

                itemName = items[0]
                tot = items[1]
                ocode = items[2]
                if type == "w":
                    print(" " + itemName, tot)
                else:
                    print(" " + itemName,ocode)
            print("[Wines]")
            for items in lstWines[0:]:

                itemName = items[0]
                tot = items[1]
                ocode = items[2]
                if type == "w":
                    print(" " + itemName, tot,ocode)
                else:
                    print(" " + itemName,ocode)
            print("[Desserts]")
            for items in lstDesserts[0:]:

                itemName = items[0]
                tot = items[1]
                ocode = items[2]
                if type == "w":
                    print(" " + itemName, tot)
                else:
                    print(" " + itemName,ocode)
# Delete
        if selction == "e":
            for items in lstEntrees[0:]:
                itemName = items[0]
                tot = items[1]
                if type == "w":
                    print(" " + itemName, tot)
                else:
                    print(" " + itemName)

        if selction == "s":
            for items in lstSides[0:]:
                itemName = items[0]
                tot = items[1]
                if type == "w":
                    print(" " + itemName, tot)
                else:
                    print(" " + itemName)
        if selction == "w":
            for items in lstWines[0:]:
                itemName = items[0]
                tot = items[1]
                if type == "w":
                    print(" " + itemName, tot)
                else:
                    print(" " + itemName)
        if selction == "d":
            for items in lstDesserts[0:]:
                itemName = items[0]
                tot = items[1]
                if type == "w":
                    print(" " + itemName, tot)
                else:
                    print(" " + itemName)

#This is for debugging purpose
"""print(menuList[2][1])

totChicken = menuList[2][1]

print("Total soup" ,totChicken)
"""











