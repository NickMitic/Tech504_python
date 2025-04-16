# Variables are symbols that point towards stored data

# Called variables as they are mutable

integer = 2
decimal = 2.1
string =  "word"

# '==' is a logical operator, asking are these two variables equal

def print_value_type(variable):
    print(f'{variable} is a {type(variable)}')

print_value_type(integer)
print_value_type(decimal)
print_value_type(string)

# Strongly typed means that all variables have a type that is set unless reassigned.
# In weakly typed languages variables data types can change without reassignment.
# E.g. a string of numbers will always be a string in Python
print_value_type("123")

# Dynamic typing means that a variable's type can change during runtime.
# In statically typed languages a variable's type is set when compiling.
# E.g. in Python we can reassign variables to different types
whatever = 'abd'
print_value_type(whatever)
whatever = True
print_value_type(whatever)

print(id(integer))
integer = 5
print(id(integer))

# Changes because the variable now points to a different object

x = 10
y = x
print(id(x))
print(id(y))

# Because they point to the same object/number

x = 11
print(id(x))
print(id(y))

# Yes, because x and y now point to different numbers

#name = input("Name please: ")
#age = input("Age please: ")
#dob = input("Date of birth please: ")
#print(f"Hi {name}, age: {age}, date of birth: {dob}")

# Operators operate upon operands

x = 5
y = 1
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

#Quotes within quotes

bad_string = "I said 'Wow!'"

print(bad_string)

bad_string = 'I said \'Wow!\''

print(bad_string)

bad_string = 'I said "Wow!"'

print(bad_string)

# Best practice is double quotes

Hw = "Hello world!"

print(Hw)

print(len(Hw))
print(Hw[0])
print(Hw[-1])
print(Hw[-2])

# This will print the string starting from the 3rd character
print(Hw[2:])
# This will print the last 3 characters
print(Hw[-3:])
# This will print up to the 5th character (inclusive)
print(Hw[:5])
# Starts from the second, stops at the fifth (doesn't include it)
print(Hw[1:4])

# Guess the word with 4 hints to help

# Rationale: Practice word slicing

# Type of exercise: Finish the code

original_word = "recommendation"

scrambled_word = "eoommandretnic"

# Create the hint slices...

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed

hint1_slice = original_word[4:6]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed

hint2_slice = original_word[-3:]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed

hint3_slice = original_word[7:10]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed

hint4_slice = original_word[:2]


# Game instructions

print("Scrambled word:", scrambled_word)

print("Guess the original word from the scrambled version.")

print("Here are some hints:")


# Hints based on list slicing

print("Hint 1: The 5th and 6th letters are '" + hint1_slice + "'.")

print("Hint 2: The last 3 letters are '" + hint2_slice + "'.")

print("Hint 3: The 8th to 10th letters are '" + hint3_slice + "'.")

print("Hint 4: The first two letters are '" + hint4_slice + "'.")

# Game ends here

print("What's your guess?")

str_with_extra_spaces = " extra spaces at the start and end "

# Write comment to explain what this does

print(len(str_with_extra_spaces))

# Write comment to explain what this does

print(len(str_with_extra_spaces.strip()))

example_text = "here's some text with some words of text"


# count how many times the substring 'text' occurs within example_text & print it to the screen

print(example_text.count('text'))

# convert example_text to lowercase & print it to the screen

print(example_text.lower())

# convert example_text to uppercase & print it to the screen

print(example_text.upper())

# capitalise the first letter in example_text & print it to the screen

print(example_text.capitalize())

# replace the word 'with' in example_text with a comma (,) instead & print it to the screen

print(example_text.replace(' with',','))

# Concatenation joins two or more strings together, e.g.
string_1 = "abc"
string_2 = "def"
print(string_1 + string_2)

x = 2

y = 5.4

z = " there's now a number 25.4 unless we put a space in!"

print(str(x) + str(y) + z)

# All variables need to be converted to strings to concatenate them

int_string = "6"


# convert int_string to an integer

integer_1 = int(int_string)

# after converting, print its data type to the screen

print(type(integer_1))

# convert int_string to float

float_1 = float(int_string)

# after converting, print its data type to the screen

print(type(float_1))

name = "Lassie"

years = 7

height_cm = 60.2


# print these variables in an f-string so that it outputs this to the screen:

# "Lassie is 7 years old and 60.2 cm tall."

print(f"{name} is {years} years old and {height_cm} cm tall")

pi = 3.14159265359


# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'

print(f"Pi to 3 decimal places: {round(pi , 3)}")

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'

print(f"Pi to 3 decimal places: {round(pi , 5)}")


score = 16

max_score = 26

score_as_decimal = score/max_score


# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)

print(f"You scored {score_as_decimal}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'

print(f"You scored {score_as_decimal * 100}%")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'

print(f"You scored {round(score_as_decimal * 100 , 2)}%")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'

print(f"You scored {round(score_as_decimal * 100)}%")

#name = input("What is your name? ")
#age = input("What is your age? ")
#month = input("What month were you born? ")
#year = input("What year were you born? ")
#print(f"Hi {name}, {age}\nYou were born in {month} of the year {year}.")

#age_int = 10
#name_str = 'Nick'
#year_born = 2025 - 10
#print(f"OMG {name_str}, you are {age_int} years old so you were born in {year_born}.")

age_int = int(input("How old are you? "))
name_str = input("What is your name? ")

birthday = ''

while birthday != 'Yes' and birthday != 'No':
    birthday = input("Have you had a birthday this calendar year? (Yes/No) ")

if birthday == 'Yes':
    year_born = 2025 - age_int
else:
    year_born = 2024 - age_int

print(f"OMG {name_str}, you are {age_int} years old so you were born in {year_born}.")

print(f"You have been alive for {age_int * 52 * 7 * 24} hours, or more.")