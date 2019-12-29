import datamuse as dm
import hashlib
import numpy as np
import textstat as tx
import PyPDF2


class User:
    def __init__(self, name, username, password, occupation):
        self.name = name
        self.username = username
        self.password = password
        self.occupation = occupation
        self.file = 'user.txt'

    def __str__(self):
        return self.name, self.username, Security.passEncrypt(self.password), self.occupation

    def regUser(self) -> None:

        with open(self.file, 'a+') as user_file:
            userList = [self.name, self.username, Security.passEncrypt(self.password), self.occupation]
            fullList = ' | '.join(userList)
            user_file.write(fullList + "\n")

        Security.passSave(self.username, Security.passEncrypt(self.password))
        return

    def createAcc(self):
        file = open(self.file, 'r')
        fileContents = file.readlines()

        dataList = []

        for i in fileContents:
            line = i.split(',')
            amount = line[1].strip('\n')
            dataList.append(amount)

        account = {}

        for i in dataList:
            for l in dataList:
                account[i] = l

    @staticmethod
    def getUser(username, db):

        with open(db, 'r') as studentFile:
            for username in studentFile:
                s = username.strip("\n")
                infoStudent = s.split(" | ")
                print(infoStudent)

            return infoStudent

    @staticmethod
    def loadUser():
        users = {}
        print("Loading Users")
        db = open("password.txt", "r")
        for line in db:
            l = line.strip("\n")
            usernamePassword = l.split(" | ")
            users[usernamePassword[0]] = usernamePassword[1]
        print("Successfully loaded " + str(len(users)) + " users.")
        return users


class Student(User):
    """
    An account object that hold the information of the user: full name, username, password

    Attributes
    -----------
    name: str
      The name of the user of the account
    username: str
      The username of the student account
    password: str
      The password of the student account


    Methods
    -------
    printName() -> None
    Prints the name of the account to the console
    printPass() -> None
    Prints the password of the account to the console
    printUser() -> None
    Prints the username of the account to the console

    """

    def __init__(self, name, username, password, occupation, school, course, grade, age, readLevel):
        """
    Constructor to build a account object

    Parameters
    ---------------
    name: str
      The name of the user of the account
    username: str
      The username of the account
    password: str
      The password of the account

    """
        super().__init__(name, username, password, occupation)
        self.school = school
        self.course = course
        self.grade = grade
        self.age = age
        self.readLevel = readLevel
        self.file = 'student.txt'

    def regStudent(self) -> None:
        with open(self.file, 'a') as user_file:
            print(super().__str__())
            userList = [self.school, self.course, self.grade, str(self.age), self.readLevel]
            fullList = list(super().__str__()) + userList
            infoList = ' | '.join(fullList)
            user_file.write(infoList + "\n")

    def __str__(self):
        return super().__str__(), self.school, self.course, self.age, self.readLevel


class Teacher(User):
    """
  The Teacher that communicates with the student about suggestions and tips for chosing and reading a book.

  Attributes
  -----------
  name: str
      The name of teacher
  degree: str
      The degree the teacher has
  years: str
      The number of years the teacher has teaching / amount of experience
  occupation: str
      The occupation at which the teacher teaches at (ie. elementary, middle, high)


  Methods
  -------
  printName() -> None
    Prints the name of the teacher to the console
  printDegree() -> None
    Prints the degrees / qualifications teacher to the console
  printYear() -> None
    Prints the years the teacher has been teaching to the console
  printOccupation() -> None
    Prints the occupation teacher teaches to the console

  """

    def __init__(self, name, username, password, occupation, degree, school, course, experience):
        """
    Constructor to build a teacher object


    Parameters
    ----------
    name: str
    The name of teacher

    degree: str
    The degree the teacher has

    years: str
        The number of years the teacher has teaching / amount of experience

    """
        super().__init__(name, username, Security.passEncrypt(password), occupation)
        self.degree = degree
        self.school = school
        self.course = course
        self.experience = experience
        self.file = 'teacher.txt'

    def regTeacher(self) -> None:
        with open(self.file, 'a+') as teacher_file:
            teacherList = [self.degree + self.school + self.course + self.experience]
            fullList = list(super().__str__()) + teacherList
            infoList = ' | '.join(fullList)
            teacher_file.write(infoList + "\n")

    def __str__(self):
        return super().__str__(), self.degree, self.school, self.course, self.experience


class Complexity:
    """
    The complexity analyzer that determines the level of complexity the text inputted into the application.

    Attributes
    -----------
    name: str
      The name of the user of the account
    username: str
      The username of the account
    password: str
      The password of the account


    Methods
    -------
    sentenceCount () -> None
      Counts the number of sentences in a text file
    wordCount() -> None
      Counts the number of words in a text file
    """

    def __init__(self, username):
        """
    Constructor to build a complexity object


    Parameters
    ----------
    fileName : str
        The name of the text file the user wish to determine the complexity of

    """

        self.username = username
        self.file = 'litFile.txt'

        return

    def sentenceCount(self) -> int:
        """
        Counts the number of sentences in a text file
        """
        periods = '.'
        sentFreq = 0

        with open(self.fileName, 'r') as file:
            fileContents = Complexity.getFileContents(self.username)

            for i in range(len(fileContents)):
                if (str(periods)) in fileContents:
                    sentFreq += 1

        return int(sentFreq)

    def wordCount(self) -> None:
        """
        Counts the amount of words in a text file
        """
        wordData = []

        with open(self.fileName, 'r') as file:
            fileContents = file.readlines()

            for words in fileContents:
                wordData += str(words)

            print(int(len(words)))
        return

    def wordChoice(self) -> None:
        with open(self.fileName, 'r') as file:
            fileContents = file.readlines()
            api = dm.Datamuse()
            api.words(rel_rhy=fileContents, max=1000)
        return

    def fleschScore(self) -> int:
        """


        """
        with open(self.fileName, 'r') as db:

            dbInfo = {}

            for line in db:
                raw = line.strip("\n")
                fileCont = raw.split(" | ")
                print(fileCont)
                dbInfo[fileCont[0]] = fileCont[1]

                if self.username in dbInfo.keys():
                    score = tx.flesch_reading_ease(dbInfo[self.username])

                return score


class Security:
    """
    The complexity analyzer that determines the level of complexity the text inputted into the applcation.

    Attributes
    -----------
    name: str
      The name of the user of the account
    username: str
      The username of the account
    password: str
      The password of the account


    Methods
    -------
    sentenceCount () -> None
      Counts the number of sentences in a text file
    wordCount() -> None
      Counts the number of words in a text file

    """

    def __init__(self, username, password):
        """
        Constructor to build a complexity object


        Parameters
        ----------
        username : str
            The username of the account

        password : str
            The combination of the password of the account with respect to the username

        """
        self.username = username
        self.password = password

        return

    @staticmethod
    def oganizeAcc(info) -> None:
        for i in range(1, len(info)):
            key = info[i]
            j = i - 1
            while j >= 0 and key < info[j]:
                info[j + 1] = info[j]
                j -= 1
            info[j + 1] = key

    @staticmethod
    def passEncrypt(password):
        hashPass = hashlib.sha1(str.encode(password)).hexdigest()  # convert byte to string

        return str(hashPass)

    @staticmethod
    def passSave(username, password):
        with open('password.txt', 'a') as pass_file:
            passList = [username, password]
            fullList = ' | '.join(passList)
            pass_file.write(fullList + "\n")

    def loginPass(self) -> bool:

        pass_file = open('password.txt', 'r')
        filePass = pass_file.readlines()

        for line in filePass:
            login_info = line.split(" | ")

            # convert string to byte
            if self.username == login_info[0] and hashlib.sha1(str.encode(self.password)).hexdigest() == login_info[1]:
                print("Correct")
                return True
            else:
                print(login_info[0], login_info[1])
                print(hashlib.sha1(str.encode(self.password)).hexdigest())
                print("Incorrect")
                return False

    @staticmethod
    def login(username, password, db):
        if username not in db.keys():
            print("\nInvalid Login Credentials.")
            return login()

        hashPass = hashlib.sha1(str.encode(password)).hexdigest()
        if hashPass == db[username]:
            return True
        else:
            return False


class Text:
    """
    A text file the user inputs their text into in order to be analyzed by the applciation

    Attributes
    -----------
    text: str
      The name of the file user wants to write text in

    Methods
    -------
    writeFile() -> None
      Writes text into file


    Constructor to build a text object


    Parameters
    ----------
    text : str
        The name of the text file the user wish to input in

    """

    @staticmethod
    def userOrganize(fileContents) -> None:
        for i in range(1, len(fileContents)):
            key = fileContents[i]

            j = i - 1
            while j >= 0 and key < fileContents[j]:
                fileContents[j + 1] = fileContents[j]
                j -= 1
                fileContents[j + 1] = key

    @staticmethod
    def userSearch(fileContents, x) -> None:
        for i in range(0, len(fileContents)):
            if fileContents[i] == x:
                return i

    @staticmethod
    def insertionSort(fileContents):

        # Goes through 1 to number of objects in list/end
        for i in range(1, len(fileContents)):

            # the integer in that spot of the list
            key = fileContents[i]

            # create variable for 1 below original position
            j = i - 1

            # while the number in the position above is bigger or equal to 0 and the value of the number in the old
            # position is smaller than the value of the new position move up 1
            while j >= 0 and key > fileContents[j]:
                fileContents[j + 1] = fileContents[j]
                j -= 1
            fileContents[j + 1] = key

    @staticmethod
    def bubbleSort(fileContents):
        # bubble sort
        l = len(fileContents)
        # goes through entire list
        for i in range(l):

            # Last i elements are already in place
            for j in range(0, l - i - 1):

                # goes through the list from 0 to l-i-1 and swap if the element found is greater than the next element
                if fileContents[j] > fileContents[j + 1]:
                    fileContents[j], fileContents[j + 1] = fileContents[j + 1], fileContents[j]

    @staticmethod
    def contentSearch(arr, x):
        # l is the left side of the array while r is the right side, arr is the array and x is the element we are
        # looking for in the array
        l = 0
        r = len(arr)

        if r >= l:

            mid = l + (r - l) // 2

            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binarySearch(arr, l, mid - 1, x)
            else:
                return binarySearch(arr, mid + 1, r, x)

        else:
            return -1


'''
user1 = User("bob", "bobby", "123jhdshfs", "middle school")
teacher1 = Teacher("bob", "bobby", "123jhdshfs", "masters in literature", "2", "middle school")
student1 = Student("bob", "bobby", "123jhdshfs", "middle school")
'''

'''

fileName = input('Which file would you like to open? ')

fileOne = Complexity(fileName)

userOne = Student("bob", "BBoy123", "bob321")


try:
  Text(12)
except TypeError:
  print ("Raised a TypeError as expected")
except Exception:
  print ("Some other Error popped up?")

try:
  Complexity(12)
except TypeError:
  print ("Raised a TypeError as expected")
except Exception:
  print ("Some other Error popped up?")

userOne.printName()
userOne.printUser()
userOne.printPass()
'''
