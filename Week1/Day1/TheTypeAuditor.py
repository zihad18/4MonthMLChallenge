raw_input = input("Type a number: ")
print(type(raw_input))
try:
    float_number = float(raw_input)
    print(type(float_number))
except ValueError:
    print("You does not provided a valid number!!")
