# makes class called player
class Player(object):
	def __init__(self, name,  age, goals, jereseynumber, position):
		self.name = name
		self.age = age
		self.goals = goals
		self.jereseynumber = jereseynumber
		self.position = position

# Print their information entered by the user, name  age  goals	
	def printStats(self):
		print("\n")
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.goals))
		print("Jersey Number: " + str(self.jereseynumber))
		print("Position: " + self.position)
		print(\n)
	
# when user opens a previosly exsisting file.
def saveTeam(list, filename):
	# open file
	file = open(filename + '.tmd', "w")
	# write to the file 
	for p in nlist:
		file.write(p.name + " "
		+ str(p.age) + " " 
		+ str(p.goals) + " " 
		+ str(p.jerseynumber) + " " 
		+ p.position + '\n')
	# close the file
	file.close()		

#loads the team, and adds to the list 
def loadTeam(list, filename):
	# empty list
	list  = []
	# open
	file = open(filename, "r")
	X = file.readline()
	# makes the players into a list to be read
	while X:
		X.split()
		words = X.split()
		list.append(Player(words[0], 
			words[1], 
			words[2], 
			words[3], 
			words[4]))
		X = file.readline()
	file.close()
	return list
	
# asks to load file or make new one 
print("welcome to Team Manager Deluxe!!")
print("Do you want to start with a new team or open an existing team?") 
print("(1) Start with a new team")
print("(2) Open a file for an existing team") 
user = raw_input() 

# either asks to load file or starts a new player list
if user == "2":
	print("What's the filename for your exsiting team? Enter name with .tmd extension:")
	filename = raw_input()
	list = loadTeam(filename)
	
else:
	list = []

# asks user to type in number For option

print("Enter the number of your choice.") 
print("(1) Make Player") 
print("(2) List Players") 
print("(3) Save Players") 
print("(0) Exit")
 
# asks user for input
user= raw_input()

while userchoice != "0":
	print("Enter the number of your choice.") 
	print("(1) Make Player") 
	print("(2) List Players") 
	print("(3) Save Players") 
	print("(0) Exit (save to avoid losing your team)")
	user = int(raw_input())
	
	if userchoice == "1":
# user creates a player
		print("_____________________________________")
		print("Enter FIRST Name: ")
		name = raw_input()

		print("Enter Age: ")
		age = input()

		print("Enter Goals: ")
		goals = input()
		
		print("Enter Jersey Number: ")
		jereseynumber = input()
		
		print("Enter Position: ")
		position = raw_input()
# saves name, age, and goals to their profile and adds to list
		nlist.append(Player(name, age, goals, jereseynumber, position))
		print(" ")
		print("Player Made.")
		print("_____________________________________")

# if 2, will print the player's stats -- name, age etc
	if userchoice == "2":
		print("-------------------------------------")
		print("Current List:")
		for p in list:
			p.printStats()
		print("-------------------------------------")

# if user input equals 3
# will add the new list to the loaded list and save to the same file to load later
	if userchoice == "3":
		print("What will your file be called? (include .tmd)")
		filename = raw_input()	
		saveTeam(list, filename)
		
if userchoice == "0":
	print("Bye")	
