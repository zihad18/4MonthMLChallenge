class User:
    
    def __init__(self):
        pass
    def create_db(self):
        print("db is created")

class Admin(User):
    def delete_db(self):
        print("admin db deleted")

superUser = Admin()
superUser.create_db()
superUser.delete_db()