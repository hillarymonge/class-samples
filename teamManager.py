class Player(object):
  
  def __init__(self, name, age, goals):
    self.name = name 
    self.age = age 
    self.goals = goals 
    
  def printStats(self):
    print ("name: " + self.name)
    print ("age:" + self.age)
    print ("goals: " + self.goals)
    
  myPlayers = []  
  
print ("Hello, what would you like yo do? ")  
print ("Press (1) to add a player")
print ("Press (2) to print all players")
print ("Press (0) to exit")

choice = input()

while choice != "0":
  
  if choice == "1":
    print("You picked add a player")
    print("Name:")
    name = input()
    print("Age:")
    age = input()
    print("Goals:")
    goals = input()
    
    myPlayers.append(Player(name, age, goals))  
