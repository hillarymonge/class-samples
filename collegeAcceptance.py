print ("How old are you? ")
age = int(input())

print ("What's your GPA?")
GPA = float(input())

if GPA > 3.0 and age > 16:
	print("Congrats! You are in!")
else:
	print("Sorry, guess you'll have to go to Harvard instead.")
