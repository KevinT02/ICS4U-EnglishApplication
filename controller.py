import view
from model import User, Student, Complexity


def createUser():
    userInfo = view.userAcc()
    user = User(userInfo[0], userInfo[1], userInfo[2], userInfo[3])
    user.register()
    return


def loadUserList():
    file = (open('user.txt', 'r')).readlines()

    for line in file:
        u = line.strip("\n")
        infoUser = u.split(" | ")
        s = line.strip("\n")
        infoStudent = s.split(" | ")
        users = [User(infoUser[0], infoUser[1], infoUser[2], infoUser[3]),
                 Student(infoStudent[0], infoStudent[1], infoStudent[2], infoStudent[3])]
        for user in users:
            print(user.name + ': ' + user.occupation())


def numSort(data):
    # Goes through 1 to number of objects in list/end
    for i in range(1, len(data)):

        # the integer in that spot of the list
        key = list[i]

        # create variable for 1 below original position
        j = i - 1

        # while the number in the position above is bigger or equal to 0 and the value of the number in the old
        # position is smaller than the value of the new position move up 1
        while j >= 0 and key > data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def bubbleSort(data):
    info = len(data)
    # goes through entire list
    for i in range(info):

        # Last i elements are already in place
        for j in range(0, info - i - 1):

            # goes through the list from 0 to l-i-1 and swap if the element found is greater than the next element
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def rateComplexity():
    data = Complexity('literature.txt')
    score = data.fleschScore()

    print('Reading score:' + score)

    if 90 <= score <= 100:
        print('Readability = Realy Easy')
    elif 80 <= score <= 89:
        print('Readability = Easy')
    elif 70 <= score <= 79:
        print('Readability = Fairly Easy')
    elif 60 <= score <= 69:
        print('Readability = Standard')
    elif 50 <= score <= 59:
        print('Readability = Fairly Difficult')
    elif 30 <= score <= 49:
        print('Readability = Difficult')
    elif 0 <= score <= 29:
        print('Readability = Very Confusing')
