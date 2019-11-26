from base64 import b64encode, b64decode
import datamuse as dm
import numpy as np
import textstat as tx
import PyPDF2


class User():
    def __init__(self, name, username, password, occupation, data):
        self.name = name
        self.password = password
        self.username = username
        self.occupation = occupation
        self.data = data  # the data file object uses
        super().__init__()

    def __str__(self):
        return self.name + " " + self.username + " " + self.password + " " + self.occupation

    def register(self) -> None:
        file = (open('user.txt', 'a+'))
        for i in file:
            userList = [self.name]
            fullList = ' | '.join(userList)
            i.write(fullList)
        return

    def createAcc(self):
        file = open(self.data, 'r')
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

    def __init__(self, name, username, password, occupation, course, age, readLevel):
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
        super().__init__(self, name, username, password, occupation)
        self.course = course
        self.age = age
        self.readLevel = readLevel

    def profile(self) -> None:
        userProfile = [super().__str__() + "," + self.course + "," + str(self.age)]
        user_file = open('profile.txt', 'a')
        user_file.write(str(userProfile))
        user_file.close()

    def printName(self) -> None:
        """
    Prints the name of the user to the console
    """
        print(self.name)
        return

    def recordStudent(self) -> None:
        record = np.array([])
        record.append(self.username)
        user_file = open('profile.txt', 'a')
        user_file.write(str(record))
        user_file.close()
        return

    def printPass(self) -> None:
        """
    Prints the password of the user to the console
    """
        print(self.password)
        return

    def printUser(self) -> None:
        """
    Prints the username of the user to the compile

    """
        print(self.username)
        return

    def printOccupation(self) -> None:
        """
    Prints the occupation of the user to the terminal

    """
        print(self.occupation)
        return

    def printReadLevel(self) -> None:
        """
    Prints the reading level of the user to the terminal
    """
        print(self.readLevel)
        return


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

    def register(self):
        pass

    def __init__(self, name, username, password, degree, years, occupation):
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
        super().__init__(name, username, password, occupation)

        self.degree = degree
        self.years = years

    def profile(self) -> None:
        user_array = []
        user_array.append(super().__str__() + "," + self.occupation)
        user_file = open('profile.txt', 'a')
        user_file.write(str(user_array))
        user_file.close()

    def printName(self) -> None:
        """
    Prints the name of the user to the console
    """
        print(self.name)
        return

    def printPass(self) -> None:
        """
    Prints the password of the user to the console
    """
        print(self.password)
        return

    def printUser(self) -> None:
        """
    Prints the username of the user to the compile

    """
        print(self.username)
        return

    def printOccupation(self) -> None:
        """
    Prints the occupation of the teacher to the console
    """
        print(self.occupation)
        return

    def printDegree(self) -> None:
        """
    Prints the degree teacher processes to the console

    """
        print(self.degree)
        return

    def printYear(self) -> None:
        """
    Prints the year of the teacher to the compile
    """
        print(self.years)
        return


class Complexity:
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

    def _init_(self, fileName: str):
        """
    Constructor to build a complexity object


    Parameters
    ----------
    fileName : str
        The name of the text file the user wish to determine the complexity of

    """

        self.fileName = fileName

        return

    def sentenceCount(self) -> int:
        """
        Counts the number of sentences in a text file
        """
        periods = '.'
        sentFreq = 0

        with open(self.fileName, 'r') as file:
            fileContents = file.readlines()

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

    def fleschScore(self) -> None:
        """


        """
        with open(self.fileName, 'r') as file:
            fileContents = file.readlines()
            readFile = ''.join(fileContents)
            score = tx.flesch_reading_ease(readFile)

            for i in range(1, len(fileContents)):
                key = fileContents[i]

                j = i - 1
                while j >= 0 and key < fileContents[j]:
                    fileContents[j + 1] = fileContents[j]
                    j -= 1
                    fileContents[j + 1] = key
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

    def _init_(self, username, password, data):
        """
        Constructor to build a compelxity object


        Parameters
        ----------
        username : str
            The username of the account

        password : str
            The combination of the password of the account with respect to the username

        """
        self.data = data
        self.username = username
        self.password = password

        return

    def oganizeAcc(self) -> None:
        info = self.data
        for i in range(1, len(info)):
            key = info[i]

            j = i - 1
            while j >= 0 and key < info[j]:
                info[j + 1] = info[j]
                j -= 1
            info[j + 1] = key

    def register(self) -> None:

        password = self.password
        encoded = b64encode(password.encode())  # convert byte to string
        pass_file = open('password.txt', 'a')
        pass_file.write(self.username)
        pass_file.write("|")
        pass_file.write(encoded)
        pass_file.write("\n")
        pass_file.close()

    def loginPass(self) -> bool:

        pass_file = open('password.txt', 'r')
        filePass = pass_file.readlines()

        for line in filePass:
            login_info = line.split("|")

            # convert string to byte
            if self.username == login_info[0] and self.password == b64decode(login_info[1].decode()):
                print("Correct")
                return True
            else:
                print("Incorrect")
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

    """

    def _init_(self, text: str):
        """
    Constructor to build a text object


    Parameters
    ----------
    text : str
        The name of the text file the user wish to input in

    """
        self.text = text

    def writeFile(self) -> None:
        # writes the inputted text into the desired file

        with open(self.text, "a+") as file:
            file.write('temporary input')


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
