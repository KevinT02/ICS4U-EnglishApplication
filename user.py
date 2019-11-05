from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, password, username, level):
        self.name = name
        self.password = password
        self.username = username
        self.level = level
        super().__init__()

    @abstractmethod
    def printName(self):
        pass

    @abstractmethod
    def printPass(self):
        pass

    @abstractmethod
    def printUser(self):
        pass

    @abstractmethod
    def register(self):
        return

    @abstractmethod
    def printLevel(self):
        return

