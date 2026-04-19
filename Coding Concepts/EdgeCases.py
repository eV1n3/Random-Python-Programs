# Start Assuming the code crash is false
code_crash = False

try:
    favorite_number = int(input("\nWhat's your favorite number (lower than 70): "))
except:
    print("That is NOT a number!")
    # If the code does crash, make this true
    code_crash = True

# If the code doesn't crash, execute everything else
if not code_crash:
    if favorite_number < 70:
        squared_number = favorite_number ** 2
        print(f"Your favorite number squared is: {squared_number}")
    else:
        print(f"{favorite_number} is not lower than 70 :(")