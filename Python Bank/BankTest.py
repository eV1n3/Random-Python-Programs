import os
os.system('cls')

#Start of Code

data_file = open("DataFile.txt", "a")
data_file.write(input("Type anything: ") + "\n")    #User input directly in write function
data_file.close()

#File Experimentation

#text_file = open("text_file.txt", "w")      #Writing to a txt file ("w" overrides, "a" appends, "x" creates file)
#text_file.write("Sea Doos are fun!")   #Text written to txt file
#text_file.close()                       #Txt file closed officially (could stop memory leaks)
#text_file = open("text_file.txt", "r")      #Relays information from txt file to variable
#print(text_file.read())                 #Prints information to console

#Experimental Functions

#Old Menu Code
#while (not exit):
    #menu()
    #menu_option = int(input())
    #os.system('cls')
    #switch_case(menu_option)

#For-loop Example
#test_list = ["Car", "Turtle", "Donut"]
#for i in range (0, 3):                     //first index is included, second index is excluded
#    print(test_list[i])

#Experimenting with lists
#experiment_list = [1]
#print(experiment_list)
#experiment_list += [2]
#print(experiment_list)
#experiment_list += ["Dog"]
#print(experiment_list)
#print(experiment_list[0] + experiment_list[1])
#experiment_list.append("Car")
#print(experiment_list)
#experiment_list.remove("Dog")
#print(experiment_list)
#experiment_list.append(5)
#print(experiment_list)

#Switch Case 1
#def switch_case (menu_option):
#    switcher = {
#    1: check_balance(),
#    2: make_deposit(),
#    3: make_withdrawl(),
#    4: view_transactions(),
#    5: calculate_interest(),
#    6: receive_loan(),
#    7: exit_application(),
#    }
#
#    return print("Please select a valid option")

#Switch Case 2
#def switch_case (menu_option):
#    match menu_option:
#        case "1":
#            check_balance()
#        case "2":
#            make_deposit()
#        case "3":
#            make_withdrawl()
#        case "4":
#            view_transactions()
#        case "5":
#            calculate_interest()
#        case "6":
#            receive_loan()
#        case "7":
#            exit_application()
#        case _:
#            print("Please select a valid option")