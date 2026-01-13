class User:
    def __init__(self, password):
        self.__password = password
    def showPassword(self):
        print(self.__password)
    
user = User('123')
user.showPassword()
#print(user._User__password)