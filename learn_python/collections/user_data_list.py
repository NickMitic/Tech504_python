age_int = int(input("How old are you? "))
name_str = input("What is your name? ")
dob = input("Date of birth: ")

user_details_list = [name_str,age_int,dob]

print(f"Name: {user_details_list[0]}")
print(f"Age: {user_details_list[1]}")
print(f"DOB: {user_details_list[2]}")
print(type(user_details_list[1]))

height = input("What is your height in cm? ")

user_details_list.append(float(height))
print(user_details_list[-1])