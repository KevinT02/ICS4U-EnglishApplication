from base64 import b64encode
from user import User


class Teacher(User):
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

    def __init__(self, name, username, password, degree, years, level):
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
        super().__init__(name, username, password, level)

        self.degree = degree
        self.years = years

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
       Prints the level of the teacher to the console
       '''
        print(self.level)
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
