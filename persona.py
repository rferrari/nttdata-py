print("Hellow I`m Python!")

# Welcome message
username = input("What is your name? ")
print("Hello, " + username + "!")

# Persona
print("How would you describe yourself?")

# User choices
choices = ["optimistic", "skeptical", "happy", "reserved"]
for i, choice in enumerate(choices):
    print(f"{i+1}. {choice}")

# Wait Reply
personality_choice = int(input("Enter the number of your response: "))

# Reply user 
# with fun message
# or just with his choice
if personality_choice == 1:
    print("Ah, you're a glass-half-full kind of person! ")
elif personality_choice == 2:
    print("You're a curious and analytical thinker!")
else:
    print("You are " + choices[personality_choice])

# Recovery username var
print("Nice to meet you " + username + "!")
exit(0)
