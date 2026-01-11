try:
    class User:
            def __init__(self):
                pass
            def method():
                pass


    new_user = User()


    new_user.method()
except TypeError:
    raise TypeError("You should use self on your method as first argument")

class User_:
        def __init__(self):
            pass
        def method(self):
            pass
new_user_ = User_()
new_user_.method()