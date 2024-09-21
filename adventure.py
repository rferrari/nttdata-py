print("Hellow I`m Python!")

# Welcome message
print("Hello, " + input("What is your name? ") + "!")

# Simple adventure game
print("You are in a dark room.")
print("There is a door to your left and a door to your right.")
print("")
print("Which door do you choose?")
choice = input()
if choice == "left":
    print("You've chosen the left door. It leads to a bright and sunny day!")
elif choice == "right":
    print("You've chosen the right door. It leads to a scary monster!")
else:
    print("Game Over")
    exit(1)
