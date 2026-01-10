USER = 'admin'
def admin_required(func):
    def wrapper(*args):
        global USER
        if USER != 'admin':
            raise PermissionError 
        else:
            func(*args)
        
    return wrapper
@admin_required
def check_password():
    print(f"12345678")
check_password()