#The project should simulate the operation of a restaurant.
# When I run main.py it should start by randomly generating a quantity for each of the menu items in the restaurant.
# These quantities will have to go down when customers order the menu items.
# Each customer order can contain an Entree, Side, Wine, and a Dessert.
# import fullmenu and roles
import fullmenu as fm
import roles as ro

run = True
fm.initAllLists()

while run:
	print("Welcome to the UNO restaurant ")
	Cinput = input (" Type w for Waiter, c for Customer, m for Manager ")
	print()
	if Cinput == "exit":
		run = False
	else:
		#print("get Roles")
		urt = ro.getroles(Cinput)
		print(urt)
		#fix if so it doesn't update count when W is selected.
		if Cinput == "c":
			CustInput = input ("Make your code selection, use a coma to seperate your selection ")
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
					#print("Selection E")
					if fm.getEntreeList(ckitems):
						print("Entree " + ckitems + " is not available, make another selection")
						nItemError = True
				else:
					print("Invalid Selection ")
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
						print("Invalid Selection ")
		elif Cinput == "m":
			print ("---------------------------")
			print("Manager Menu")
			print ("---------------------------")
			mgrInput = input ("Make a selection, C=Clear list N=Generate New List")
			if mgrInput == "C":
				print("Clear List")	
				fm.clrAllLists()
			elif mgrInput == "N":
				fm.initAllLists()
				mrt = ro.getroles("w")
				print (mrt)
		elif Cinput == "w":
			print ("---------------------------")
			print("Waiter Menu")
			print ("---------------------------")
			
		else: 
			print("Invalid Option, try again")
			print()
