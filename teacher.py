from abc import ABC
from base64 import b64encode
from user import User


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

   """

    def register(self):
        pass

    def __init__(self, name, username, password, years, level, degree):
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
        level: str
           The level at which the teacher teaches at (ie. elementary, middle, high)

        """
        super().__init__(name, username, password, level)

        self.degree = degree
        self.years = years

    def profile(self) -> None:
        user_array = []
        user_array.append(super().__str__() + "," + self.degree + "," + self.years)
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

    def printLevel(self) -> None:
        """
        Prints the level of the teacher to the console
        """
        print(self.level)
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
