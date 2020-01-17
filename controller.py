import view as v
from model import User, Student, Complexity, Teacher, Login


def loginCheck(username, password):
    # dictionary for account and password
    db = User.loadUser()
    print(db)
    account = Login(username, password, db)
    result = account.login()

    if result == "True":
        print("Access granted. Welcome " + username + ".")
        userInfo = User.getUser(username, 'user.txt')
        return ['True', userInfo]

    elif result == "Exist" or result == "False":
        return ['False', 'incorrect']


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
        return "Very Easy"
    elif 80 <= score <= 89:
        return "Easy"
    elif 70 <= score <= 79:
        return "Fairly Easy"
    elif 60 <= score <= 69:
        return "Standard"
    elif 50 <= score <= 59:
        return "Fairly Difficult"
    elif 30 <= score <= 49:
        return "Difficult"
    elif 0 <= score <= 29:
        return "Very Advanced"
    return


def dataUpload(general, specific):
    data = [general, specific]
    User.uploadData(data)
    return


def run():
    while True:
        begin = v.GUI.begin()
        if begin:
            userInfo = loginCheck(begin[1], begin[2])
            print('begin', str(userInfo))
            print(userInfo[1])

            if userInfo[0] == 'True':
                info = userInfo[1]
                if 'Student' in info:

                    data = v.GUI.displayInfo(userInfo[1], User.getUser(info[0], 'student.txt'))
                    if data == 'Document':
                        v.GUI.popFile(userDoc(info[0]))
                    elif data == 'Flesch score':
                        score = rateComplexity(userInfo[0])
                        print(score)
                    else:
                        continue

                elif 'Teacher' in info:
                    v.GUI.displayInfo(userInfo[1], User.getUser((info[0]), 'teacher.txt'))
                    break
            elif userInfo[0] == 'False':
                v.GUI.incorrectPopup()
                continue

        if not begin:
            userInfo = v.GUI.userAcc()
            createUser(userInfo)
            if userInfo[3] == 'Student':
                studentInfo = v.GUI.studentAcc()
                createStudent(userInfo, studentInfo)
                dataUpload(userInfo, studentInfo)
                continue
            elif userInfo[3] == 'Teacher':
                teacherInfo = v.GUI.teacherAcc()
                createTeacher(userInfo, teacherInfo)
                dataUpload(userInfo, teacherInfo)
                continue
