
def cache(func):
    dict = {}
    def wrapper(*args):
        query = args[0]
        if query in dict:
            return dict[query]
        else:
            result = func(*args)
            dict[query] = result

         #   print(f"inside wrapper {dict}")
            return result
    return wrapper

@cache
def prime_checker(num):
    
    print('inside function')
    if num%2 == 0:
        return False
    
    i = 3
    while True:
        if num % i == 0:
            return False
        i += 2
        if i * i > num:
            return True

@cache 
def check_palindrom(text):
    print(f"inside function")
    return text == text[::-1]
print(prime_checker(5))
print(prime_checker(8))
print(prime_checker(6))
print(prime_checker(5))

print(check_palindrom("madam"))
print(check_palindrom("doll"))