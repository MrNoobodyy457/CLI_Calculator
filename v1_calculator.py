def calculator():
    print("This is a calculator")

    error1 = "The entered value is not a number."

    while True:
        I = input("First Number: ")
        if I.lower() in ["n", "no", "stop"]:
            break

        II = input("Second Number: ")
        if II.lower() in ["n", "no", "stop"]:
            break

        try:
            num1 = float(I)
            num2 = float(II)
        except ValueError:
            print(error1)
            continue

        operation = input("Select an operation [+, -, *, /, ^, root(r)]: ")

        try:
            if operation.lower() in ["n", "no", "stop"]:
                break

            if operation == "+":
                print("Answer:", num1 + num2)

            elif operation == "-":
                print("Answer:", num1 - num2)

            elif operation == "root" or operation == "r":
                try:
                    print("Answer:", num1 ** (1/num2))
                except ZeroDivisionError:
                    print("Cannot calculate root with zero as the second number.")
                    continue
            elif operation == "*":
                print("Answer:", num1 * num2)

            elif operation == "/":
                try:
                    print("Answer:", num1 / num2)
                    print("Quotient:", num1 // num2)
                    print("Remainder:", num1 % num2)
                except ZeroDivisionError:
                    print("Division by zero is not allowed.")
                    continue
            elif operation == "^":
                print("Answer:", num1 ** num2)

            else:
                print("The entered operation does not exist.")
                continue
        except OverflowError:
            print('''The result is too large to be represented.
Please try with smaller numbers.''')
            continue

        cont = input('''Do you want to continue? 
(Press enter to continue or type 'N' to stop): ''')
        if cont.lower().strip() in ["n", "no", "stop"]:
            print("Thanks for using")
            break


calculator()
