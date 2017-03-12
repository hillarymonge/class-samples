# a Player on a team has a name, an age, and a number of goals so far this season
class Player(object):

	def __init__(self, name, age, goals, jersey_number, position):
		self.name = name
		self.age = age
		self.goals = goals
		self.jersey_number = jersey_number
		self.position = position

	def printStats(self):
		print("\n")
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.goals))
		print("Jersey Number: " + str(self.jersey_number))
		print("Position: " + str(self.position))
		print("\n")





# takes the playerList and the user's desired filename
# writes each Player to file
def saveTeam(playerList, filename):
	# open the file
	my_file = open(filename + '.tmd', 'w')

	# write to the file
	for p in playerList:
		my_file.write(p.name + ' ' 
				+ str(p.age) + ' '
				+ str(p.goals) + ' '
				+ str(p.jersey_number) + ' '
				+ p.position + '\n')

	# close the file
	my_file.close()





# takes a filename for a file of players
# returns a list of Players
def loadTeam(filename):

	# empty list
	my_players = []
	# open the file
	my_file = open(filename, 'r')

	# read each line and create Player from it
	line = my_file.readline()
	while line:
		# split each line into a list of the variables
		player = line.split()
		my_players.append(Player(player[0],
			player[1],
			player[2],
			player[3],
			player[4]))
		# read the next line
		line = my_file.readline()

	# close the file
	my_file.close()

	# return the completed list
	return my_players



# when starting, see if the user wants to load a team
print("Welcome to Team Manager Deluxe!")
print("Do you want to start with a new team or open an existing team?")
print("Enter the # of your choice and press Enter.")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")
user_choice = int(raw_input())

if user_choice == 2:
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
	filename = raw_input()
	my_players = loadTeam(filename)
else:
	my_players = []

while user_choice != 0:
	print("What do you want to do? Enter the # of your choice and press Enter.")
	print("(1) Add a player")
	print("(2) Print all players")
	print("(3) Print average number of goals for all players")
	print("(4) Save your player list to a file")
	print("(0) Leave the program (save first to avoid losing your data!)")
	user_choice = int(raw_input())

	# if the user wants to add a player, collect their data and make a Player object
	if user_choice == 1:
		print("Enter name:")
		player_name = raw_input()
		print("Enter age:")
		player_age = int(raw_input())
		print("Enter number of goals scored this season:")
		player_goals = int(raw_input())
		print("Enter the jersey number worn by this player:")
		jersey_num = int(raw_input())
		print("Enter the position that this player plays:")
		position = raw_input()
		my_players.append(Player(player_name, player_age, player_goals, jersey_num, position))
		print("Ok, player entered.")

	# if the user wants to print the players, call printStats for each Player
	if user_choice == 2:
		print("Here are all the players...")
		for player in my_players:
			player.printStats()
	
	if user_choice == 3:
		# average = sum of all goals divided by count of players
		sum = 0
		count = 0
		for player in my_players:
			sum += player.goals
			count += 1
		avg = sum / count

		print("Average goals: " + str(avg))
	
	if user_choice == 4:
		print("Ok, what would you like to name the file? We'll add on a .tmd file extension to whatever you enter.")
		filename = raw_input()
		saveTeam(my_players, filename)
