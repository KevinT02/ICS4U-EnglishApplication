from base64 import b64encode
from user import User


class Student(User):
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

    def __init__(self, name, username, password, level):
        '''
        Constructor to build a account object

        Parameteres
        ---------------
        name: str
          The name of the user of the account
        username: str
          The username of the account
        password: str
          The password of the account

        '''
        super().__init__(self, name, username, password, level)

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

    def printLevel(self) -> None:

        '''
        Prints the academic level of the user to the compile

        '''
        print(self.level)
        return




