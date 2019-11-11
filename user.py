
class User():
    def __init__(self, name, password, username, level, occupation):
        self.name = name
        self.password = password
        self.username = username
        self.level = level
        self.occupation = occupation
        super().__init__()

    def printName(self):
        pass

    def __str__(self):
        return self.name + " " + self.username + " " + self.password + " " + self.level

    def printName(self):
        pass

    def printPass(self):
        pass

    def printUser(self):
        pass

    def register(self):
        return

    def printLevel(self):
        return
