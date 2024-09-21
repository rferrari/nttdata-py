print("Hellow I`m Python!")

# Welcome message
username = input("What is your name? ")
print("Hello, " + username + "!")

# User choices
choices = ["optimistic", "skeptical", "happy", "reserved"]
while True:
    # Persona
    print(username + ", How would you describe yourself?")

    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    # Wait Reply
    try:
        personality_choice = int(input(username + " Whats your persona?"))
    except ValueError:
        print("Invalid input "+ username + ". Please enter a number.")
        print("")
        continue

    if 1 <= personality_choice <= len(choices):
        break
    else:
        print("Invalid choice. Please try again.")
        print("")

print("")

# Reply user 
# with fun message
# or just with his choice
if personality_choice == 1:
    print("Ah, you're a glass-half-full kind of person! ")
elif personality_choice == 2:
    print("You are a curious thinker!")
else:
    print("Ah, you're a " + choices[personality_choice-1] + " kind of person! ")

print("Nice to meet you " + username + "!")
exit(0)
