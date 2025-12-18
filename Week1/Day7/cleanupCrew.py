try:
    a = int(input("Enter a number: "))
    b = int(input('Enter a number: '))
    divide = a/b
except ZeroDivisionError:
    print('not permissible')
finally:
    print("Execution Complete")