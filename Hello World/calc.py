def menu():
    print("--------------------")
    print("Please select one of the following")
    print("Basic Calculator : 1")
    print("Loan Calculator : 2")
    print("--------------------")

def basic_calc(equation):
    separated_equation = equation.split()
    numbers = []
    arithmetic = []
    for entry in separated_equation:
        if entry.isdigit():
            numbers.append(int(entry))
        elif entry.isalpha():
            print(f"{entry} shouldn't be here")
        else:
            for check in ["+", "-", "*", "/"]:
                if entry is check:
                    arithmetic.append(entry)
                    break

def loan_calc():
    pass

basic_calc("/-+*!@#$")