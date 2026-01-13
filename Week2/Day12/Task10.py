class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def __eq__(self,other):
        if self.name == other.name and self.id == other.id:
            return True
        else:
            return False

user1 = User('zihad',3)
user2 = User('zihad',3)
print(user1 == user2)