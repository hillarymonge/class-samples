# contacts.py
# rc.monge.hillary [at] leadps.org

print("Welcome to Contacts!")
Choice=1
myContacts={}

print("Enter the number of your choice.")

while Choice != 0:
	print("Press (0) Exit the Contacts app")
	print("Press (1) Add a phone number")
	print("Press (2) Print the full list of contacts")
	print("Press (3) Enter a name to retrieve that contact's phone number")

	Choice=int(raw_input())
	
	if Choice == 1:
		print("Enter a name for your contact?")
		name = raw_input()
		print("Enter a phone number for your contact?")
		num= raw_input()	

		myContacts[name]= num

	if Choice == 2:
		print(myContacts)

	if Choice == 3:
		print("Whose number would you like to see?")
		name= raw_input()
		print("This is the person you were looking for:")
		print(myContacts[name])
