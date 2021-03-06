import datamuse as dm
import hashlib
import textstat as tx
from PyPDF2 import PdfFileReader


class User:
    """
        An account object that hold the information of the user: full name, username, password, occupation

        Attributes
        -----------
        name: str
            The name of the user of the account

        username: str
            The username of the user account

        password: str
            The password of the user account

        occupation: str
            The occupation of the user account, whether the individual is a student of teacher


        Methods
        -------
        regUser() -> None
            Calls the passSave function that saves the password into the security database and saves the general account
            information associated with the user
        uploadData() -> None
            Uploads string containing all the information associated with the account
        getUser() -> string
            Returns the account information associated with username input
        getDoc() -> string
            Returns document associated with the username input
        loadUser() -> tuple
            Returns the account information held within the database
        __str__() -> string
            Returns a string containing the general information about the user

        """

    def __init__(self, name, username, password, occupation):
        """
        Constructor to build a user object

        Parameters
        ----------
        name : str
            The name of the user
        username : str, optional
            The username of the user
        password : str
            The password associated with the account
        occupation : str, optional
            The occupation the user, Student or Teacher
            Student if nothing selected

        """

        self.name = name
        self.username = username
        self.password = password
        self.occupation = occupation
        self.file = 'user.txt'

    def __str__(self):
        """
        Creates a string containing general user information including password, occupation, username and name of user
        """
        return self.name, self.username, Security.passEncrypt(self.password), self.occupation

    def regUser(self) -> None:
        """
        Creates a list of information for the user account and saves it in the user database and uses passSave function
        to save account and password in security database

        """
        with open(self.file, 'a+') as user_file:
            userList = [self.name, self.username, Security.passEncrypt(self.password), self.occupation]
            fullList = ' | '.join(userList)
            user_file.write(fullList + "\n")

        Security.passSave(self.username, Security.passEncrypt(self.password))
        return

    @staticmethod
    def uploadData(infoList):
        """
        Takes all information associated with an account and writes it into the account database containing every
        piece of information that had been inputted by user

        Parameters
        ----------
        infoList : list
            The account information contained within a list

        """
        with open('userDatabase.txt', 'a+') as userData:
            userData.write(str(infoList))
            userData.write("\n")
        return

    @staticmethod
    def getUser(username, db):
        """
        Attempts to read the information in the database and look for the username that was given and return the
        information associated with it

        Parameters
        ----------
        username : str
            The username to look for in the database.
        db : str
            The database to look for the user in.

        Returns
        -------
        string
            Returns the information associated with the account

        """

        with open(db, 'r') as studentFile:
            infoStudent = ""

            for info in studentFile:
                if username in info:
                    s = info.strip("\n")
                    infoStudent = s.split(" | ")

            return infoStudent

    @staticmethod
    def getDoc(username, db):
        """
        Attempts to read the information in the database and look for the username that was given and return the
        document associated with it

        Parameters
        ----------
        username : str
            The username to look for in the database.
        db : str
            The database to look for the user in.

        Returns
        -------
        string
            Returns the document associated with the account

        """
        studentFile = open(db, encoding="utf8")
        data = ''.join(studentFile)
        infoStudent = data.split(" | ")
        for info in infoStudent:
            if info == username:
                return infoStudent[1]

    @staticmethod
    def loadUser():
        """
        Attempts to load all the users contained within the database along with the passwords and put them in a
        dictionary and return the dictionary for other functions to use when verifying password.

        Returns
        -------
        dictionary
            A dictionary containing various accounts and the correct passwords associated with it

        """
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
        The username of the user account
    password: str
        The password of the user account
    occupation: str
        The occupation of the user account, whether the individual is a student of teacher
    school: str
      The school the student is currently attending
    course: str
      The course code of the course the student is currently in
    grade: str
      The grade the student is currently in
    age: str
      The age of the student
    readLevel: str
      The reading level of the student


    Methods
    -------
    regStudent() -> None
        Takes the information of the student, puts it in a list and writes it into the database
    __str__() -> None
        Returns a string containing the attributes of the object

    """

    def __init__(self, name, username, password, occupation, school, course, grade, age, readLevel):
        """
        Constructor to build a user object

        Parameters
        ----------
        school: str
            The school the student is currently attending
        course: str
            The course code of the course the student is currently in
        grade: str
            The grade the student is currently in
        age: str
            The age of the student
        readLevel: str
            The reading level of the student
        file : str
            The database information is taken from

        """
        super().__init__(name, username, password, occupation)
        self.school = school
        self.course = course
        self.grade = grade
        self.age = age
        self.readLevel = readLevel
        self.file = 'student.txt'

    def regStudent(self) -> None:
        """
        Registers the students into the student database

        """
        with open(self.file, 'a') as user_file:
            print(super().__str__())
            userList = [self.school, self.course, self.grade, str(self.age), self.readLevel]
            fullList = list(super().__str__()) + userList
            infoList = ' | '.join(fullList)
            user_file.write(infoList + "\n")
        return

    def __str__(self):
        """
        Creates a string containing all the information about the student
        """
        return super().__str__(), self.school, self.course, self.age, self.readLevel


class Teacher(User):
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

    def __init__(self, name, username, password, occupation, degree, school, course, experience):
        """
        Constructor to build a teacher object

        Parameters
        ----------
        degree: str
            The degrees the teacher currently posses
        school: str
            The school the teacher is currently teaching at
        course : str
            The course code the teacher is currently teaching
        experience : str
            The years of experience the teacher has in the education field

        """
        super().__init__(name, username, Security.passEncrypt(password), occupation)
        self.degree = degree
        self.school = school
        self.course = course
        self.experience = experience
        self.file = 'teacher.txt'

    def regTeacher(self) -> None:
        """
        Registers teacher information into the teacher account database
        """
        with open(self.file, 'a+') as teacher_file:
            teacherList = [self.degree + self.school + self.course + self.experience]
            fullList = list(super().__str__()) + teacherList
            infoList = ' | '.join(fullList)
            teacher_file.write(infoList + "\n")

    def __str__(self):
        """
        A string containing information about the teacher object
        """
        return super().__str__(), self.degree, self.school, self.course, self.experience


class Discover:
    """
        A class containing functions that organize and analyze text


        Methods
        -------
        contentSearch() -> str
            Uses binary search to look for user content in database return location
        userSearch() -> str
            Uses linear search to look for user in database return location

        """

    def __init__(self, fileContents, info):
        """
        Constructor to build a Complexity object

        Parameters
        ----------
        fileContents: list
            The username that will be looked for in the document database to return the correct password associated
            with the username
        info: str
            The password that will be verified with the password that the user input

        """

        self.fileContents = fileContents
        self.info = info

    def contentSearch(self):
        # l is the left side of the array while r is the right side, arr is the array and x is the element we are
        # looking for in the array
        content = self.fileContents
        x = self.info
        l = 0
        r = len(content)

        while r >= l:

            mid = l + (r - l) // 2

            if content[mid] == x:
                return mid
            elif content[mid] > x:
                mid -= 1
                return mid
            else:
                mid += 1
                return mid

        else:
            return -1

    def userSearch(self) -> None:
        x = self.info
        content = self.fileContents
        for data in range(0, len(content)):
            if content[data] == x:
                return data


class Complexity:
    """
    An account object that hold the information of the user: full name, username, password

    Attributes
    -----------
    username: str
      The username of the account that the will be looked for in the database
    file: str
      The file name of database that will be analysed

    Methods
    -------
    sentenceCount() -> None
        Prints the name of the account to the console
    wordCount() -> None
        Prints the password of the account to the console
    wordChoice() -> None
        Uses the datamuse api to find appropriate synonyms for words to increase writing quality
    fleschScore() -> int
        Analyses text using the flesch score algorithm and returns an integer containing the score of the complexity of
        the piece of literature

    """

    def __init__(self, username, file):
        """
        Constructor to build a Complexity object

        Parameters
        ----------
        username: str
            The username that will be looked for in the document database to return a document text or file

        """

        self.username = username
        self.fileName = file
        self.default = 'litFile.txt'

    def sentenceCount(self) -> int:
        """
        Counts the amount of sentences within a file

        """

        periods = '.'
        sentFreq = 0

        fileContents = Discover(User.getDoc(self.username), periods).contentSearch

        for i in range(len(fileContents)):
            if (str(periods)) in fileContents:
                sentFreq += 1

        return int(sentFreq)

    def wordCount(self) -> None:
        """
        Counts the amount of words within a file

        """

        wordData = []

        with open(self.default, 'r') as file:
            fileContents = file.readlines()

            for words in fileContents:
                wordData += str(words)

            print(int(len(words)))
        return

    def wordChoice(self) -> None:
        """
        Uses the datamuse api that suggest changes that will grammatically enhance the writing

        """
        with open(self.default, 'r') as file:
            fileContents = file.readlines()
            api = dm.Datamuse()
            api.words(rel_rhy=fileContents, max=1000)
        return

    def fleschScore(self) -> int:
        """
        Uses the textstat api to determine how complex a piece of literature is based on the flesch score algorithm
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
    An object that holds information about the user's/account's security information which includes username and
    password

    Attributes
    -----------
    username: str
      The username of the student account
    password: str
      The password of the student account


    Methods
    -------
    organizeAcc() -> None
        Prints the name of the account to the console
    passEncrypt() -> str
        Prints the password of the account to the console
    passSave() -> None
        Prints the username of the account to the


    """

    def __init__(self, username, password):
        """
        Constructor to build a Complexity object

        Parameters
        ----------
        username: str
            The username that will be looked for in the document database to return the correct password associated
            with the username
        password: str
            The password that will be verified with the password that the user input

        """

        self.username = username
        self.password = password

    def passEncrypt(self):
        password = self.password
        """
        Uses a hash library to convert the password the user input to hash in order to ensure security of account
        """
        hashPass = hashlib.sha1(str.encode(password)).hexdigest()  # convert byte to string

        return str(hashPass)

    def passSave(self):
        """
        Saves the password in hash into the account password database
        """
        username = self.username
        password = self.password

        with open('password.txt', 'a') as pass_file:
            passList = [username, password]
            fullList = ' | '.join(passList)
            pass_file.write(fullList + "\n")
        return


class Login:
    """
        An object that holds information about the user's/account's security information which includes username and
        password

        Attributes
        -----------
        username: str
          The username of the student account
        password: str
          The password of the student account


        Methods
        -------
        organizeAcc() -> None
            Prints the name of the account to the console
        passEncrypt() -> str
            Prints the password of the account to the console
        passSave() -> None
            Prints the username of the account to the
        login() -> string
            Prints the username of the account to the console


        """

    def __init__(self, username, password, db):
        """
        Constructor to build a Complexity object

        Parameters
        ----------
        username: str
            The username that will be looked for in the document database to return the correct password associated
            with the username
        password: str
            The password that will be verified with the password that the user input

        """

        self.username = username
        self.password = password
        self.db = db

    def login(self):
        """
        looks through the password data base and converts the password the user inputted into hash and compares the
        password in hash associated with the username and returns a boolean based on the comparison.

        """
        username = self.username
        password = self.password
        db = self.db

        hashPass = hashlib.sha1(str.encode(password)).hexdigest()
        if username not in db.keys():
            print('exist')
            return "Exist"
        elif hashPass == db[username]:
            print('true')
            return "True"
        else:
            return "False"


class PDF:
    """
        A class containing functions that organize and analyze text


        Methods
        -------
        getText() -> str
            Read the PDF file and returns a string containing text from the PDF

        """

    def __init__(self, location):
        """
        Constructor to build a PDF object

        Parameters
        ----------
        location: str
            The location which the file is located for the PyPDF2 api to extract text from

        """

        self.location = location

    def getText(self):
        """
        Using the PyPDF2 api, the pdf file is analysed. It skims and reads the text and converts it into a string for
        the program to use.

        """
        with open(self.location, 'rb') as f:
            pdf = PdfFileReader(f)

            # get the first page
            page = pdf.getPage(1)
            print(page)
            print('Page type: {}'.format(str(type(page))))

            text = page.extractText()
        return text


class Text:
    """
    A class containing functions that organize and analyze text


    Methods
    -------
    userOrganize() -> None
        Organize users in the database
    insertionSort() -> None
        Sorts database using the insertion sort algorithm
    bubbleSort() -> None
        Sorts database using the bubble sort algorithm

    """

    def __init__(self, fileContents):
        """
        Constructor to build a Complexity object

        Parameters
        ----------
        fileContents: str
            The list that the program will be sorting through and organize using various algorithms

        """

        self.fileContents = fileContents

    def userOrganize(self) -> None:
        content = self.fileContents
        for i in range(1, len(content)):
            key = content[i]

            j = i - 1
            while j >= 0 and key < content[j]:
                content[j + 1] = content[j]
                j -= 1
                content[j + 1] = key

    def insertionSort(self):
        content = self.fileContents
        # Goes through 1 to number of objects in list/end
        for i in range(1, len(content)):

            # the integer in that spot of the list
            key = content[i]

            # create variable for 1 below original position
            j = i - 1

            # while the number in the position above is bigger or equal to 0 and the value of the number in the old
            # position is smaller than the value of the new position move up 1
            while j >= 0 and key > content[j]:
                content[j + 1] = content[j]
                j -= 1
            content[j + 1] = key

    def bubbleSort(self):
        content = self.fileContents
        # bubble sort
        l = len(content)
        # goes through entire list
        for i in range(l):

            # Last i elements are already in place
            for j in range(0, l - i - 1):

                # goes through the list from 0 to l-i-1 and swap if the element found is greater than the next element
                if content[j] > content[j + 1]:
                    content[j], content[j + 1] = content[j + 1], content[j]
