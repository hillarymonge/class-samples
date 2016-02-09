# prints welcome to haiku chooser and gives the user the options 
print ("Welcome to Haiku, chooser!")
print ("Choose..")
print ("(1) for a Haiku about")
print ("(2) for a Haiku about")

# makes a variable for the user input 
choice = input()

# makes two variables that will open up the two text files with the haikus
haiku1 = open('haiku1.txt', 'r')
haiku2 = open('haiku2.txt', 'r')

# makes a loop with the if statement 
if choice == 1:
	# Prints out haiku number 1
	print (haiku1.read())

# creats an elif loop so that if the choice is 2 the user gets the second haiku.
elif choice == 2:
	print(haiku2.read())

