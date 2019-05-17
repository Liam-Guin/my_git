import os,sys,time

sl = []
try:
	f = open("shopping2.txt","r")
	for line in f:
		sl.append(line.strip())
	f.close()
except:
	pass
	
os.system('cls' if os.name == 'nt' else 'clear')

def mainScreen():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("   SHOPPING LIST / MAIN MENU")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n")
	print("Your shopping list currently contains",len(sl),"items :)")
	print("\n\n")
	print("Please choose one of the following options:")
	print("\n")
	print(" a  (add to the list)")
	print(" d  (delete from the list)")
	print(" v  (view the list)")
	print(" q  (quit the program)")
	print("\n\n")
	choice = input("Choice: ")
	if len(choice) > 0:
		if choice.lower()[0] == "a":
			addScreen()
		elif choice.lower()[0] == "d":
			deleteScreen()
		elif choice.lower()[0] == "v":
			viewScreen()
		elif choice.lower()[0] == "q":
			sys.exit()
		else:
			mainScreen()
	else:
		mainScreen()


def addScreen():
	print(sl) 
	os.system('cls' if os.name == 'nt' else 'clear')
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("   ADD ITEM(S)")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n\n")
	print("Please type the name of the item that you want to add.")
	print("\n")
	print("  (or press ENTER to return to the main menu)")
	print("\n\n")
	item = input("Item: ")
	if len(item) > 0:
		sl.append(item)
		print("Item added :)")
		saveList()
		time.sleep(0.2)
		addScreen()
	else:
		mainScreen()


def viewScreen():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("   VIEW LIST")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n")
	for item in sl:
		print(item)
	print("\n")
	print("  (press ENTER to return to the main menu)")
	print("\n")
	input()
	mainScreen()
	

def deleteScreen():
	global sl
	os.system('cls' if os.name == 'nt' else 'clear')
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("   DELETE ITEM(S)")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n")
	count = 0
	for item in sl:
		print(count, " - ", item)
		count = count + 1
	print("\n")
	print("What number on the list would you like to delete?")
	print("\n")
	print("  (or press ENTER to return to the main menu)")
	print("\n\n")
	choice = input("Number: ")
	if len(choice) > 0:
		try:
			del sl[int(choice)]
			print("Item deleted...")
			saveList()
			time.sleep(0.2)
		except:
			print("Invalid number")
			time.sleep(0.2)
		deleteScreen()
	
	else:
		mainScreen()
		
def saveList():
		f = open("shopping2.txt", "w")
		for item in sl:
			f.write(item+"\n")
		f.close()
			
	
mainScreen()