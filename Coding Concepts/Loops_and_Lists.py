# For Loop
for number in range(1, 11):
    print(number)

# While Loop
condition = "please"
user_input = input("What's the magic word? ")
while not user_input == condition:
    print("Nope!")
    user_input = input("What's the magic word? ")

print("That's correct!")

# Basic Lists
todo = ["Breathe", "Make breakfast", "Drive to CISO","Attend CISO", "Drive back home"]
completed = []
for task in todo:
    print(task)
    completed.append(task)
    print(completed)

# Tree
for number in range(1, 8):
    leaf = "*"
    print(number * leaf)