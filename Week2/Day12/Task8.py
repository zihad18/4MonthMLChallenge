class User:
    
    def __init__(self):
        print("base user called")
    def create_db(self):
        print("db is created")

class Admin(User):
    def __init__(self):
        super().__init__()
        print("its now inhereted admin class")


    def delete_db(self):
        print("admin db deleted")

admin = Admin()
