import random

pastas = open('user.txt', 'r')
pastaArray = pastas.readlines()
infoList = []

for i in range(0, 100000):

    prices = (open('age.txt', 'w'))
    userList = pastaArray[random.randint(0, 399)]

    infoList.append(userList)

    joinedList = ''.join(infoList)
    b = joinedList.split('\n')

    for i in b[:-1]:
        price = int(str(random.randint(0, 100)))
        prices.write(i + ' | ' + str(price) + '\n')
