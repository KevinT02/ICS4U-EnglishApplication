from base64 import b64encode

import numpy as np

from user import User


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

    def __init__(self, name, username, password, level, course):
        """
        Constructor to build a account object

        Parameteres
        ---------------
        name: str
          The name of the user of the account
        username: str
          The username of the account
        password: str
          The password of the account

        """
        super().__init__(name, username, password, level)
        self.course = course

    def profile(self) -> None:
        user_array = []
        user_array.append(super().__str__() + "," + self.course)
        user_file = open('profile.txt', 'a')
        user_file.write(str(user_array))
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

    def printLevel(self) -> None:
        """
        Prints the academic level of the user to the compile

        """
        print(self.level)
        return
