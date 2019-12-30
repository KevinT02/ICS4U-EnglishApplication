def getDoc(username, db):
    studentFile = open(db, encoding="utf8")
    data = ''.join(studentFile)
    infoStudent = data.split(" | ")
    print(infoStudent)
    for info in infoStudent:
        if info == username:
            print(infoStudent[1])




getDoc('k', 'litFile.txt')
