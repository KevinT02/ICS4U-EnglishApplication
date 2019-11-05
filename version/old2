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
import pip

from teacher import Teacher
from user import User
from student import Student

user1 = User("bob", "bobby", "123jhdshfs", "middle school")
teacher1 = Teacher("bob", "bobby", "123jhdshfs", "masters in literature", "2", "middle school")
student1 = Student("bob", "bobby", "123jhdshfs", "middle school")


def nameInput():
    layout = [
        [sg.Text('Please enter your Name, Address, Phone')],
        [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
        [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
        [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Simple data entry window').Layout(layout)
    button, values = window.Read()

    print(button, values[0], values[1], values[2])
    return


class Security:
    '''
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

       '''

    def _init_(self, username, password):
        '''
           Constructor to build a compelxity object


           Parameters
           ----------
            username : str
               The username of the account
            password : str
               The combination of the password of the account with respect to the username

         '''

        self.username = username
        self.password = password

        return

    def register(self) -> None:

        password = self.password
        encoded = b64encode(password.encode())
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
            if self.username == login_info[0] and self.password == b64decode(login_info[1].decode()):
                print("Correct")
                return True
            else:
                print("Incorrect")
                return False


class Complexity:
    '''
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


user = Student('bob', 'charlie', 123)
user.nameInput()
'''
