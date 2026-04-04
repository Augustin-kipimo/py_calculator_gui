print("SSIMPLE CALCULATOR")
print("Select one operater from the following list:")
print("1. + addition")
print("2. - subtraction")
print("3. * multiplication")
print("4. / division")
operator = input("Enter your choice (1/2/3/4): ")
if operator == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if num1.isnumeric() and num2.isnumeric():
        result = int(num1) + int(num2)
        print(" The result is: ", result)

elif operator == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if num1.isnumeric() and num2.isnumeric():
        result = int(num1) - int(num2)
        print(" The result is: ", result)
    else:
        print("Invalid input. Please enter numeric values.")

elif operator == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if num1.isnumeric() and num2.isnumeric():
        result = int(num1) * int(num2)
        print(" The result is: ", result)
    else:
        print("Invalid input. Please enter numeric values.")

elif operator == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if num1.isnumeric() and num2.isnumeric():
        if num2 == "0":
            print("Error: Division by zero is not allowed.")
            #num2 = input("Enter second number that is greater than is not equal to ): ")
        else:
            result = float(num1) / float(num2)
            print(" The result is: ", result)
    else:
        print("Invalid input. Please enter numeric values.")
else:
    print("Invalid operation. please select a valid operator (1/2/3/4).")