import view as v
from model import User, Student, Complexity, Teacher, Security


def loginCheck(username, password):
    db = User.loadUser()
    print(db)
    result = Security.login(username, password, db)
    while True:
        if result:
            print("Access granted. Welcome " + username + ".")
            userInfo = User.getUser(username, 'user.txt')
            return userInfo
        elif not result:
            print("Invalid Login Credentials.")


def createUser(userInfo):
    userSave = User(userInfo[0], userInfo[1], userInfo[2], userInfo[3])
    userSave.regUser()
    return userInfo


def createTeacher(userInfo, teacherInfo):
    teacherSave = Teacher(userInfo[0], userInfo[1], userInfo[2], userInfo[3], teacherInfo[0], teacherInfo[1],
                          teacherInfo[2], teacherInfo[3])
    teacherSave.regTeacher()
    return teacherSave


def createStudent(userInfo, studentInfo):
    studentSave = Student(userInfo[0], userInfo[1], userInfo[2], userInfo[3], studentInfo[0], studentInfo[1],
                          studentInfo[2], studentInfo[3], studentInfo[4])
    studentSave.regStudent()
    return studentSave


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
    return


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
    return


def bubbleSort(data):
    info = len(data)
    # goes through entire list
    for i in range(info):

        # Last i elements are already in place
        for j in range(0, info - i - 1):

            # goes through the list from 0 to l-i-1 and swap if the element found is greater than the next element
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return


def rateComplexity(username):
    data = Complexity(username)
    score = data.fleschScore(data)

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
    return


def run():
    begin = v.GUI.begin()
    if begin:
        userInfo = loginCheck(begin[1], begin[2])
        viewInfo = ('Name: ' + userInfo[0] + '\n' + 'User: ' + userInfo[1] + '\n' + 'Password: ' + userInfo[2] + '\n' + 'Occupation: ' + userInfo[3])

        if 'Student' in viewInfo:
            v.GUI.displayInfo(viewInfo, User.getUser('student.txt'))

        elif ' Teacher' in viewInfo:
            v.GUI.displayInfo(viewInfo, User.getUser('teacher.txt'))

    elif not begin:
        userInfo = v.GUI.userAcc()
        createUser(userInfo)
        if userInfo[3] == 'Student':
            studentInfo = v.GUI.studentAcc()
            createStudent(userInfo, studentInfo)
        elif userInfo[3] == 'Teacher':
            teacherInfo = v.GUI.teacherAcc()
            createTeacher(userInfo, teacherInfo)
        return
