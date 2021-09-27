#The project should simulate the operation of a restaurant.
# When I run main.py it should start by randomly generating a quantity for each of the menu items in the restaurant.
# These quantities will have to go down when customers order the menu items.
# Each customer order can contain an Entree, Side, Wine, and a Dessert.
#import roles as r
import fullmenu as fm
import roles as ro

run = True
while run:
 print(" Welcome to the UNO restaurant ")
 Cinput = input ("Type w for Waiter, c for Customer, m for Manager ")
 if Cinput == "exit":
    run = False
 else:
  urt = ro.getroles(Cinput)
 print(urt)
 #fix if so it doesn't update count when W is selected.
 if Cinput == "c":
  CustInput = input ("Make your selection, make sure you use a  coma to seperate your selection ")
  orList = list(CustInput.split(","))
 for items in orList[0:]:
  mnSel = items[0:1]
  if mnSel == "W":
    # This is for debugging purpose
    print("Selection W" )
    for wcode in fm.lstWines[0:]:
        if wcode[2] == items:
         print("Original Wine number" + str(wcode[1]))
         wcode[1] = wcode[1]-1
         print ("Wine Updated number"+ str(wcode[1]))
  elif mnSel == "D":
      # This is for debugging purpose
      print("Selection D")
  elif mnSel == "S":
      # This is for debugging purpose
      print("Selection S")
  elif mnSel == "E":
      print("Selection E")
      for ecode in fm.lstEntrees[0:]:
          if ecode[2] == items:
              print("Original Entree number" , ecode[1])
              ecode[1] = ecode[1] - 1
              print("EntreeUpdated number", ecode[1])
  else:
      print("Invalid Selection ")













