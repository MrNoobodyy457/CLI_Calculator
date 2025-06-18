def calculator():
    print("This is a calculator")

    error1 = "The entered value is not a number."
    histroy = []

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
        if operation.lower() in ["n", "no", "stop"]:
            break

        if operation == "+":
            answer = num1 + num2
            print("Answer:", answer)

        elif operation == "-":
            answer = num1 - num2
            print("Answer:", answer)

        elif operation == "root" or operation == "r":
            try:
                answer = num1 ** (1/num2)
                print("Answer:", answer)
            except ZeroDivisionError:
                print("Cannot calculate root with zero as the second number.")
                continue
        elif operation == "*":
            answer = num1 * num2
            print("Answer:", answer)

        elif operation == "/":
            try:
                answer = num1 / num2
                print("Answer:", answer)
                print("Quotient:", num1 // num2)
                print("Remainder:", num1 % num2)
            except ZeroDivisionError:
                print("Division by zero is not allowed.")
                continue
        elif operation == "^":
            answer = num1 ** num2
            print("Answer:", answer)

        else:
            print("The entered operation does not exist.")
            continue
        histroy.append(f"{num1} {operation} {num2} = {answer}")

        cont = input('''Do you want to continue?
(Press enter to continue) 
(Enter 'H' for history)
(Enter 'C' for clear history)
(Enter 'N' to stop): ''')
        if cont.lower() in ["n", "no", "stop"]:
            print("Thanks for using")
            break
        elif cont.lower() in ["c", "clear"]:
            histroy.clear()
            print("History cleared.")
            cont = input('''Do you want to continue?
(Press enter to continue)
(Enter 'N' to stop): ''')
        elif cont.lower() in ["history", "h", "his"]:
            print("Calculation History:")
            for entry in histroy:
                print(entry)
            cont = input('''Do you want to continue? 
(Press enter to continue)
(Enter 'N' to stop): ''')
        if cont.lower() in ["n", "no", "stop"]:
            print("Thanks for using")
            break


calculator()
