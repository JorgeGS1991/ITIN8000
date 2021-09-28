# Add full menu
# Entrees, Sides, Wine and Desserts
import random as r

# import roles

# This is a list
# def menu():
lstEntrees = []
lstSides = []
lstWines = []
lstDesserts = []


def initAllLists():
    lstEntrees.append(["Chicken ", r.randint(1, 6), "E1"])
    lstEntrees.append(["Beef ", r.randint(1, 6), "E2"])
    lstEntrees.append(["Vegetarian ", r.randint(1, 6), "E3"])
    # Sides List
    lstSides.append(["Soup ", r.randint(5, 10), "S1"])
    lstSides.append(["Salad ", r.randint(5, 10), "S2"])
    # Wine List
    lstWines.append(["Merlot ", r.randint(2, 5), "W1"])
    lstWines.append(["Chardonnay ", r.randint(2, 5), "W2"])
    lstWines.append(["Pinot ", r.randint(2, 5), "W3"])
    lstWines.append(["Rose ", r.randint(2, 5), "W4"])
    # Desserts List
    lstDesserts.append(["Flan ", r.randint(1, 3), "D1"])
    lstDesserts.append(["Creme_brulee ", r.randint(1, 3), "D2"])
    lstDesserts.append(["Chocolate_moose ", r.randint(1, 3), "D3"])
    lstDesserts.append(["Cheesecake ", r.randint(1, 3), "D4"])


'''def initializeList():
	lstEntrees = [["Chicken ", r.randint(1, 6), "E1"],
             ["Beef ", r.randint(1, 6), "E2"],
             ["vegetarian ", r.randint(1, 6), "E3"]]
	lstSides = [["soup ", r.randint(5, 10), "S1"],
             ["salad ", r.randint(5, 10), "S2"]]
	lstWines = [
             ["Merlot ", r.randint(2, 5), "W1"],
             ["chardonnay ", r.randint(2, 5), "W2"],
             ["pinot ", r.randint(2, 5), "W3"],
             ["rose ", r.randint(2, 5), "W4"]]
	lstDesserts = [
             ["flan ", r.randint(1, 3), "D1"],
             ["creme_brulee ", r.randint(1, 3), "D2"],
             ["chocolate_moose ", r.randint(1, 3), "D3"],
             ["cheesecake ", r.randint(1, 3), "D4"]
             ]'''


def clrAllLists():
    lstEntrees.clear()
    lstDesserts.clear()
    lstWines.clear()
    lstSides.clear()


# This is for debugging purpose
"""    print("Avalable in Menu")
    for items in fmenuList[0:]:
        itemName = items[0]
        tot = items[1]
        print(itemName, tot)
        """


# Selection  parm is for *, e, s, d
# type par is for w,c
def prtMenuList(selction, type):
    if selction == "*":
        print("[Entrees]")
        for items in lstEntrees[0:]:
            itemName = items[0]
            tot = items[1]
            ocode = items[2]
            if type == "w":
                print(" " + itemName, "-", tot)
            else:
                print(" " + itemName, "Code -", ocode)

        print("[Sides]")
        for items in lstSides[0:]:

            itemName = items[0]
            tot = items[1]
            ocode = items[2]
            if type == "w":
                print(" " + itemName, "-", tot)
            else:
                print(" " + itemName, "Code -", ocode)
        print("[Wines]")
        for items in lstWines[0:]:

            itemName = items[0]
            tot = items[1]
            ocode = items[2]
            if type == "w":
                print(" " + itemName, "-", tot)
            else:
                print(" " + itemName, "Code -", ocode)
        print("[Desserts]")
        for items in lstDesserts[0:]:

            itemName = items[0]
            tot = items[1]
            ocode = items[2]
            if type == "w":
                print(" " + itemName, "-", tot)
            else:
                print(" " + itemName, "Code -", ocode)
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


def updWineList(item):
    for wcode in lstWines[0:]:
        if wcode[2] == item:
            # print("Original Wine number" + str(wcode[1]))
            wcode[1] = wcode[1] - 1
        # print ("Wine Updated number"+ str(wcode[1]))


def updEntreeList(item):
    for ecode in lstEntrees[0:]:
        if ecode[2] == item:
            ecode[1] = ecode[1] - 1


def updSidesList(item):
    for scode in lstSides[0:]:
        if scode[2] == item:
            scode[1] = scode[1] - 1


def updDessertList(item):
    for dcode in lstDesserts[0:]:
        if dcode[2] == item:
            dcode[1] = dcode[1] - 1


def getWineList(item):
    zeroLeft = False
    for wcode in lstWines[0:]:
        if wcode[2] == item:
            # print("Original Wine number" + str(wcode[1]))
            if wcode[1] == 0:
                zeroLeft = True
    return zeroLeft


# print ("Wine Updated number"+ str(wcode[1]))
def getEntreeList(item):
    zeroLeft = False
    for ecode in lstEntrees[0:]:
        if ecode[2] == item:
            if ecode[1] == 0:
                zeroLeft = True
    return zeroLeft


def getSidesList(item):
    zeroLeft = False
    for scode in lstSides[0:]:
        if scode[2] == item:
            if scode[1] == 0:
                zeroLeft = True
    return zeroLeft


def getDessertList(item):
    zeroLeft = False
    for dcode in lstDesserts[0:]:
        if dcode[2] == item:
            if dcode[1] == 0:
                zeroLeft = True
    return zeroLeft


# This is for debugging purpose
"""print(menuList[2][1])
totChicken = menuList[2][1]
print("Total soup" ,totChicken)
"""
