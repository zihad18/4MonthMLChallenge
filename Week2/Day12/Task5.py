from datetime import date
class User:

    def __init__(self):
        self.__birthYear = 2004
    
    @property
    def take(self):
        return date.today().year - self.__birthYear
user = User()
val = user.take
print(val)