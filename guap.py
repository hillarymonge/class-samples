# for every roll of paper towles, you get a $0.25 rebate 
# but if you buy more than 10 rolls, you get a $0.25 rebate for each on

# but if you are a club member, you get a $2 rebate for buying at least one 

# find out if user a value club member 
print ("Are you a value club member? Respond yes or no.")
club = (raw_input())

# find out how many rolls of paper towles user bought 
print ("how many rolls of paper towles did you buy?")
rolls = int(raw_input())

if club == "yes":
	if rolls > 10:
		 rebate = rolls * .35 + 2
	else:
		 rebate = rolls * .25 + 2
else:
	

# print rebate
print("Your rebate is $" + str(rebate))
