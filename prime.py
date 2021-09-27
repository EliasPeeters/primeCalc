import random

# z11 = input('1. Zahl? ')
# z22 = input('2. Zahl? ')
# z11 = int(z11)
# z22 = int(z22)


def probablyprime(number):
    a = random.randint(1, number-1)
    if ggt(number, a) != 1:
        return False
    if (a ** (number-1)) % number != 1:
        return False
    return True


def prime(number, iteration):

    for x in range(iteration):
        if not probablyprime(number):
            return 1
    return 0.5 ** iteration


def ggt(z1, z2):
    if z1 == 0:
        print(z2)
    else:
        while z2 != 0:
            if z1 > z2:
                z1 = z1 - z2
            else:
                z2 = z2 - z1
    return z1


primes = []

lastPrime = 2
run = True
last_line = 2

with open("data.txt", "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass

print(last_line)
lastPrime = int(last_line) + 1

while run:
    if prime(lastPrime, 20) != 1:
        f = open("data.txt", "a")
        f.write(str(lastPrime) + '\n')
        f.close()
    lastPrime += 1

