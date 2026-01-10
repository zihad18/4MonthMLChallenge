def bold(func):
    def wrapper(*args):
        #function_output = str(func(*args))
        return "<b>" + func(*args) + "</b>"
    return wrapper
def italic(func):
    def wrapper(*args):
       # function_output = str(func(*args))
        return "<i>" + func(*args) + "</i>"
    return wrapper
@bold
@italic
def say_hello(name):
    return "Hello " + name
print(say_hello("Sami"))