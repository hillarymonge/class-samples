# applycipher.py 
# imports needed
import string

# applyCipher.py
# A program to encrypt/decrypt user text using Caesar's Cipher

# Author: rc.monge.hillary [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet 
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	alphabet = string.ascii_lowercase
	UpperAlpha = string.ascii_uppercase
	print(UpperAlpha)
	Edic = {}
	for l in range(0, len(alphabet)):
		Edic[UpperAlpha[(l + key) % 26]] = UpperAlpha[l] 	
	for l in range(0, len(alphabet)):
		Edic[alphabet[(l + key) % 26]] = alphabet[l]
		Edic[" "] = " "
	return Edic


# gets the encrypted message from the user
# arguments: none
# returns: encoded message
def getMessage():
	print("What is the message you would like to decode?")
	message = input()
	return message	


# for each letter in message, deocdes and records
# arguments: encoded message, dictionary 
# returns: decoded message 
def decodeMessage(message, dictionary):
	newMessage = ""
	for l in message:
		newMessage = newMessage + dictionary[l] 
	return newMessage

	
# outputs the decoded message to the terminal
# arguments: decoded message
# returns: non
def printMessage(message):
	print(message)

# execution starts here

# asks for the key 
try:
	print("What is your key to decode?")
	key = int(input())

	dictionary = createDictionary(key)
	encodedMessage = getMessage()
	decodedMessage = decodeMessage(encodedMessage, dictionary)
	print("This is your secret message:")
	printMessage(decodedMessage)
	
except: 
	print("**Sorry we have encounterd an error**")
