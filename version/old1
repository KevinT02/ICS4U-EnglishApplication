# -----------------------------------------------------------------------------
# Name:        Main Program (mainProgram.py)
# Purpose:     To demonstrate understanding of
# Author:      Kevin Tu
# Created:     25-Sep-2019
# Updated:     14-Oct-2019
# -----------------------------------------------------------------------------

from base64 import b64encode, b64decode
import PySimpleGUI as sg
import PyPDF2



class Student:
    '''
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
    '''

    def __init__(self, name, username, password):
        '''
        Constructor to build a account object

        Parameters
        ---------------
        name: str
          The name of the user of the account
        username: str
          The username of the account
        password: str
          The password of the account

        '''
        self.name = name
        self.username = username
        self.password = password


    def printName(self) -> None:

        '''
        Prints the name of the user to the console
        '''
        print(self.name)
        return

    def printPass(self) -> None:

        '''
        Prints the password of the user to the console
        '''
        print(self.password)
        return

    def printUser(self) -> None:

        '''
        Prints the username of the user to the compile

        '''
        print(self.username)
        return

    def register(self) -> None:

        string = self.password
        encode = b64encode(string.encode())
        file = open('password.txt', 'a')
        file.write(self.username)
        file.write(" ")
        file.write(encode)
        file.write("\n")
        file.close()

    def loginPass(self) -> bool:

        file = open('password.txt', 'r')
        filePass = file.readlines()

        for line in filePass:
            login_info = line.split()
            if self.username == login_info[0] and self.password == b64decode(login_info[1].decode()):
                print("Correct")
                return True
            else:
                print("Incorrect")
                return False

    def nameInput(self) -> None:
        layout = [
            [sg.Text('Please enter your full Name, Username, Password')],
            [sg.Text('Name', size=(15, 1)), sg.InputText()],
            [sg.Text('Username', size=(15, 1)), sg.InputText()],
            [sg.Text('Password', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('window').Layout(layout)
        button, values = window.Read()

        print(button, values[0], values[1], values[2])
        print(self.name)
        return


class Teacher:
    '''
    The Teacher that communicates with the student about suggestions and tips for chosing and reading a book.

    Attributes
    -----------
    name: str
        The name of teacher
    degree: str
        The degree the teacher has
    years: str
        The number of years the teacher has teaching / amount of experience
    level: str
        The level at which the teacher teaches at (ie. elementary, middle, high)


   Methods
   -------
   printName() -> None
     Prints the name of the teacher to the console
   printDegree() -> None
     Prints the degrees / qualifications teacher to the console
   printYear() -> None
     Prints the years the teacher has been teaching to the console
   printLevel() -> None
     Prints the level teacher teaches to the console

   '''

    def __init__(self, name, degree, years, level):
        '''
        Constructor to build a teacher object


        Parameters
        ----------
        name: str
        The name of teacher
        degree: str
        The degree the teacher has
        years: str
           The number of years the teacher has teaching / amount of experience
        level: str
           The level at which the teacher teaches at (ie. elementary, middle, high)

        '''

        self.name = name
        self.degree = degree
        self.years = years
        self.level = level

    def printName(self) -> None:
        '''
        Prints the name of the teacher to the console
        '''
        print(self.name)
        return

    def printDegree(self) -> None:
        '''
        Prints the degree teacher processes to the console

        '''
        print(self.degree)
        return

    def printYear(self) -> None:
        '''
        Prints the year of the teacher to the compile
        '''
        print(self.years)
        return

    def printLevel(self) -> None:
        '''
        Prints the level of the teacher to the console
        '''
        print(self.level)
        return


class Complexity:
    '''
    The complexity analyzer that determines the level of complexity the text inputted into the applcation.

    Attributes
    -----------
    fileName: str
        The name of the file the user would like to open and use
   Methods
   -------
   sentenceCount () -> None
     Counts the number of sentences in a text file
   wordCount() -> None
     Counts the number of words in a text file

   '''

    def _init_(self, fileName: str):
        '''
        Constructor to build a compelxity object

        Parameters
        ----------
        fileName : str
        The name of the text file the user wish to determine the complexity of

        '''

        self.fileName = open(fileName, "r")

        return

    def sentenceCount(self) -> None:
        '''
        Counts the number of sentences in a text file
        '''
        fileContents = self.fileName.readlines()
        periods = '.'

        sentenceData = []

        for i in range(0, len(fileContents), 1):
            if periods in fileContents[i]:
                sentenceData.append(i)
                x = len(sentenceData)
                print(i)
        print(x)

    def wordCount(self) -> None:
        '''
        Counts the amount of words in a text file
        '''

        fileContents = self.fileName.readlines()

        wordData = []

        for words in fileContents:
            wordData += words
        print(len(wordData))
        return


class Text:
    '''
   A text file the user inputs their text into in order to be analyzed by the applciation

   Attributes
   -----------
   text: str
       The name of the file user wants to write text in

   Methods
   -------
   writeFile() -> None
     Writes text into file

   '''

    def _init_(self, text: str):
        '''
        Constructor to build a text object


        Parameters
        ----------
        text : str
            The name of the text file the user wish to input in

        '''
        self.text = text

    def writeFile(self) -> None:
        '''
        writes the inputted text into the desired file
        '''

        with open(self.text, "a+") as file:
            file.write('temporary input')


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

'''
float - can no exceed 15 digits, decimal numbers of 16 digits can be accurately represented as a float, 32 Bits



string - can not exceed 63 GB

byte - can not exceed 8 Bits

doubles - 64 bytes, 16 - 17 stig FloatingPointError

'''
user = Student('fullname', 'name', 'password')
user.nameInput()

    def sentenceCount(self) -> None:
        '''
       Counts the number of sentences in a text file
       '''
        fileContents = self.fileName.readlines()
        periods = '.'

        sentenceData = []

        for i in range(0, len(fileContents), 1):
            if periods in fileContents[i]:
                sentenceData.append(i)
                x = len(sentenceData)
                print(i)
        print(x)

    def wordCount(self) -> None:
        '''
       Counts the amount of words in a text file
       '''
        fileContents = self.fileName.readlines()

        wordData = []

        for words in fileContents:
            wordData += words
        print(len(words))
        return


class Text:
    '''
   A text file the user inputs their text into in order to be analyzed by the applciation

   Attributes
   -----------
   text: str
       The name of the file user wants to write text in

   Methods
   -------
   writeFile() -> None
     Writes text into file

   '''

    def _init_(self, text: str):
        '''
           Constructor to build a text object


           Parameters
           ----------
           text : str
               The name of the text file the user wish to input in

           '''
        self.text = text

    def writeFile(self) -> None:
        '''
       writes the inputted text into the desired file
       '''

        with open(self.text, "a+") as file:
            file.write('temporary input')


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

'''
float - can no exceed 15 digits, decimal numbers of 16 digits can be accurately represented as a float, 32 Bits



string - can not exceed 63 GB

byte - can not exceed 8 Bits

doubles - 64 bytes, 16 - 17 stig FloatingPointError

'''
user = Student('bob', 'charlie', 123)
user.loginPass()
