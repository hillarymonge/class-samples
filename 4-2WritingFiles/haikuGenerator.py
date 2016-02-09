# welcomes user to the program and asks for the three lines of their haikus
print ("Welcome to the Haiku Generator!")
print ("Provide your first line of your Haiku:")
firstline = raw_input()
print ("Provide your second line of your Haiku:")
secondline = raw_input()
print ("Provide your third line of your Haiku:")
thirdline = raw_input()

# asks user for a name for the file in which they want their haikus
print ("Make a file to store your Haiku in, what would you like to name it:")
filename = raw_input()

# makes a list of the users Haiku lines together
usersHaiku = [firstline , secondline, thirdline]

# makes the file where user will store their Haiku
userfile = open(filename, "a")

# writes the three lines into the file
for line in usersHaiku:
	userfile.write(line + "/n")

# tells the user what to do to see their Haiku
print ("Done, to view your Haiku type 'cat' and the name of your file in the command line.")
print ("When you run this in the command line you should get your Haiku.")

# closes the file that is the users
userfile.close()
