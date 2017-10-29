print "\nThis is a simple calculator!\n\nTry to calculate something.\n\nYou can use +, -, * and / .\n"
while True:
    while True:
        try:
            a = float(raw_input("\nYour first number: "))
            break
        except:
            print "\nThat was not a number. Try again.\n"
            continue
    while True:
        try:
            b = float(raw_input("\nYour second number: "))
            break
        except:
            print "\nThat was not a number. Try again.\n"
            continue
    while True:
        calculation = raw_input("\nChoose +, -, * or /: ")
        if calculation == "+":
            print "\nThe answer is: ", a + b, "\nCalculate something else."
            break
        elif calculation == "-":
            print "\nThe answer is: ", a - b, "\nCalculate something else."
            break
        elif calculation == "*":
            print "\nThe answer is: ", a * b, "\n\nCalculate something else."
            break
        elif calculation == "/":
            print "\nThe answer is: ", a / b, "\nCalculate something else."
            break
        else:
            print "\nSomething went wrong... Try again.\n"