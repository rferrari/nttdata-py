# consts
LIMIT_DAYLY = 100
LIST_STATES = [
    "STATE1",
    "STATE2",
    "STATE3",
    "STATE4",
]

# vars
userName = "my name"
userAge = 21

userName = "other name"
print(userName, userAge)

# thats interesting...
userName, userAge = "anna", 28

print(userName, userAge)
print(LIMIT_DAYLY)
print(LIST_STATES)

# carefull, const can change, lol
LIST_STATES = "none"
print(LIST_STATES)

