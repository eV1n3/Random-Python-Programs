# integer_example = 1
# double_example = 6.7
# boolean_example = True
# character_example = "x"
# string_example = "hello"

# user_age = int(input("Input your age: "))
# if user_age < 18:
#     print("Access denied!")
# else:
#     print("You are now an adult!")

def age_checker(age):
    if age < 18:
        print("Access denied!")
    else:
        print("You are now an adult!")

age_checker(48)
age_checker(67)
age_checker(14)
age_checker(-1)
age_checker(18)