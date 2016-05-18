
# applycipher.py 
# a program to encrypt/decrypt user text using Caesar's Cipher

# Author: rc.monge.hillary [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet 
# arguments: key
# returns: dictionary of mapped letters 
def creatDictionary(key):
    
    # placeholder
    return {}

# asks user for encoded messege 
# arguments: none
# returns: encoded messege
def getMessage():
    
    pass

# for each letter in message, deocdes and records
# arguments: encoded message, dictionary 
# returns: decoded message 
def decodeMessage(message, dictionary):
    pass
    
# outputs the decoded message to the terminal
# arguments: decoded message
# returns: non
def printMessage(message):
    pass

# execution starts here 

# ask user for the key 
print("What key would you like to use to decode?")
key = int(raw_input())

dictionary = creatDictionary(key) 
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedmessage, dictionary)

printMessage (decodedMessage)


