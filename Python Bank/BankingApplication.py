import os
os.system('cls')

#Variables
balance = 100
menu_option = 0
exit = False
log_book = []
transactions = []
INTEREST = 0.01     #Consistent 1% interest rate per month
loan = 0
debt = False
debt_amount = 0.0

#Methods
def menu():
    os.system('cls')
    print("1 - Check Balance\n2 - Make a Deposit\n3 - Make a Withdrawl"+
    "\n4 - View Previous Transactions\n5 - Calculate Interest\n6 - Receive Loan\n7 - Exit Application")

def switch_case(menu_option):       #Psuedo Switch Case
    if(menu_option == 1):
        check_balance()
    elif(menu_option == 2):
        make_deposit()
    elif(menu_option == 3):
        make_withdrawl()
    elif(menu_option == 4):
        view_transactions()
    elif(menu_option == 5):
        calculate_interest()
    elif(menu_option == 6):
        receive_loan()
    elif(menu_option == 7):
        exit_application()
    else:
        print("Please select a valid option")

def history(log, transaction):
    global log_book
    global transactions
    log_book.append(log)
    transactions.append(transaction)

def check_balance():
    global balance
    balance = round(balance, 2)
    print("Your balance is: $" + str(balance) + "\n")
    os.system('pause')

def make_deposit():
    global balance
    global log_book
    global transactions

    #Deposit Error Checker
    error = True
    while(error):
        try:
            deposit = round(float(input("Amount you would like to deposit: $")), 2)
            if (deposit < 0.01):
                os.system('cls')
                print("Please select more than $0.01\n")
                os.system('pause')
                os.system('cls')
            else:
                error = False
        except:
            os.system('cls')
            print("Please select a valid option\n")
            os.system('pause')
            os.system('cls')

    balance += deposit
    print("Your current balance is: $" + str(balance) + "\n")

    history("Deposited", deposit)
    os.system('pause')

def make_withdrawl():
    global balance
    global log_book
    global transactions

    #Withdrawl Error Checker
    error = True
    while(error):
        try:
            withdrawl = round(float(input("Amount you would like to withdrawl: $")), 2)
            if (withdrawl < 0.01):
                os.system('cls')
                print("Please select more than $0.01\n")
                os.system('pause')
                os.system('cls')
            elif (balance - withdrawl < 0):
                os.system('cls')
                print("You can't take more than you have")
                print("You currently have $" + str(balance) + "\n")
                os.system('pause')
                os.system('cls')
            else:
                error = False
        except:
            os.system('cls')
            print("Please select a valid option\n")
            os.system('pause')
            os.system('cls')

    balance -= withdrawl
    print("Your current balance is: $" + str(balance) + "\n")

    history("Withdrew", withdrawl)
    os.system('pause')

def view_transactions():
    global log_book
    global transactions

    for i in range(0, len(log_book)):
        print(
            str(log_book[i]) + ": --> $" + str(transactions[i])
        )
    print("\n")
    os.system('pause')

def calculate_interest():
    global INTEREST
    temporary_investment = 0

    #Interest Error Checker
    error = True
    while(error):
        try:
            initial_investment = round(float(input("Amount you would like to invest: $")), 2)
            if (initial_investment < 0.01):
                os.system('cls')
                print("Please select more than $0.01\n")
                os.system('pause')
                os.system('cls')
            else:
                error = False
        except:
            os.system('cls')
            print("Please select a valid option\n")
            os.system('pause')
            os.system('cls')

    investment_with_interest = initial_investment
    os.system('cls')

    #Month Error Checker
    error = True
    while(error):
        try:
            months = int(input("Amount of months: "))
            if (months <= 0):
                os.system('cls')
                print("Please select more than 0 months\n")
                os.system('pause')
                os.system('cls')
            else:
                error = False
        except:
            os.system('cls')
            print("Please select a valid option\n")
            os.system('pause')
            os.system('cls')
    os.system('cls')

    for i in range (0, months):
        temporary_investment = investment_with_interest * INTEREST
        investment_with_interest += temporary_investment
    
    print("Initial Investment: $" + str(round(initial_investment, 2)))
    print("Investment w/ Interest: $" + str(round(investment_with_interest, 2)))
    print("\n")
    os.system('pause')

def receive_loan():
    global loan
    global log_book
    global transactions
    global INTEREST
    global balance
    global debt
    global debt_amount

    if(not debt):
        #Loan Error Checker
        error = True
        while(error):
            try:
                loan = round(float(input("Amount you wish to borrow: $")), 2)
                if (loan < 0.01):
                    os.system('cls')
                    print("Please select more than $0.01\n")
                    os.system('pause')
                    os.system('cls')
                elif (loan > 500000):
                    os.system('cls')
                    print("Please select an amount under or equivalent to $500,000\n")
                    os.system('pause')
                    os.system('cls')
                else:
                    error = False
            except:
                os.system('cls')
                print("Please select a valid option\n")
                os.system('pause')
                os.system('cls')

        balance += loan
        debt_amount = round(float(loan + (loan * INTEREST * 12)), 2)
        print("The money has been added to your account.\n")
        print("You owe a total of $" + str(debt_amount))
        print("You have 1 year to pay.\n")
        
        debt = True
        history("Loan", loan)
        os.system('pause')
    else:
        print("You owe $" + str(debt_amount) + " before you can recieve another loan.\n")
        os.system('pause')

def exit_application():
    global exit
    exit = True

#Start of Code
login_attempts = 3
while(login_attempts > 0 and not exit):
    pin_number = str(input("Pin: "))
    if (pin_number == "2213"):
        while (not exit):
            #Experimental Error Catcher Menu
            menu()
            try:
                menu_option = int(input())
            except:
                os.system('cls')
                print("Please select a valid option\n")
                os.system('pause')
            os.system('cls')
            switch_case(menu_option)
    else:
        login_attempts -= 1
        if(login_attempts <= 0):
            os.system('cls')
            print("You have been locked out for 24hrs.\n")
        else:
            os.system('cls')
            print("You have " + str(login_attempts) + " login attempts left.\n")
            os.system('pause')
            os.system('cls')