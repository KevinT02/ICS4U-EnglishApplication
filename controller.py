import view as v
from model import User, Student, Complexity, Teacher, Security


def loginCheck(username, password):
    # dictionary for account and password
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


def userDoc(username):
    fileContent = User.getDoc(username, 'litFile.txt')
    return fileContent


def createUser(userInfo):
    userSave = User(userInfo[0], userInfo[1], userInfo[2], userInfo[3])
    userSave.regUser()
    return userInfo


def createTeacher(userInfo, teacherInfo):
    teacherSave = Teacher(userInfo[0], userInfo[1], userInfo[2], userInfo[3], teacherInfo[0], teacherInfo[1],
                          teacherInfo[2], teacherInfo[3])
    teacherSave.regTeacher()
    return teacherSave


def userDatabase(generalInfo, specificInfo):
    database = [generalInfo, specificInfo]
    n = 0
    for item in database:
        n += 1
        information = ""
        information += item[n]
        for info in information:
            infoList = ' | '.join(info)
            return infoList


def createStudent(userInfo, studentInfo):
    studentSave = Student(userInfo[0], userInfo[1], userInfo[2], userInfo[3], studentInfo[0], studentInfo[1],
                          studentInfo[2], studentInfo[3], studentInfo[4])
    studentSave.regStudent()
    return studentSave


def rateComplexity(username):
    data = Complexity(username)
    score = data.fleschScore(data)

    print('Reading score:' + score)

    if 90 <= score <= 100:
        print('Readability = Really Easy')
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


def dataUpload(general, specific):
    User.uploadData(userDatabase(general, specific))
    return


def run():
    begin = v.GUI.begin()
    if begin:
        userInfo = loginCheck(begin[1], begin[2])
        print('begin' + str(userInfo))

        if 'Student' in userInfo:
            x = v.GUI.displayInfo(userInfo, User.getUser(userInfo[0], 'student.txt'))
            if x == 'Document':
                v.GUI.popFile(userDoc(userInfo[0]))

        elif ' Teacher' in userInfo:
            v.GUI.displayInfo(userInfo, User.getUser(userInfo[0], 'teacher.txt'))

    elif not begin:
        userInfo = v.GUI.userAcc()
        createUser(userInfo)
        if userInfo[3] == 'Student':
            studentInfo = v.GUI.studentAcc()
            createStudent(userInfo, studentInfo)
            dataUpload(userInfo, studentInfo)
        elif userInfo[3] == 'Teacher':
            teacherInfo = v.GUI.teacherAcc()
            createTeacher(userInfo, teacherInfo)
            dataUpload(userInfo, teacherInfo)
        return
