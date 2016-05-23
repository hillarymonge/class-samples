def isPrime(my_num):
        for n in range(2,my_num):
                if my_num % n == 0:
                        return False
        return True
print ("this is true")
print (isPrime(11))
print ("this is false")
print (isPrime(10))
listt = []
for number in range(2,10001):
        y = isPrime(number)
        if y == True:
                listt.append(number)
                myfile = open("primes.txt", "w")
                myfile.write(str(listt) + "/n")

print(listt)

myfile.close()
