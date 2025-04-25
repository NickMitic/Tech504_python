user_prompt = True
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 118:
        user_prompt = False
    else:
        print("Please enter an integer, or a sensible age.")
print(f"Your age is {age}")