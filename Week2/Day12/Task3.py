class User:
    def __init__(self):
        self.name = "Mahi"
    def __str__(self):
        return f"User: {self.name}"
    def __repr__(self):
        return f"User: {self.name} repr"
obj = User()
print(obj)
print(repr(obj))