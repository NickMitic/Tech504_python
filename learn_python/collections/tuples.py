# Tuples also store multiple objects in a certain order
# Yes they are immutable, their values cannot be changed after assignment
# Int, Float, String
# Tuples are faster, more secure
# Prints the tuple then counts the amount of items in it = "bread"

print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")

essentials_tuple = (essential_item1,essential_item2,essential_item3)

print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")

essentials_list = list(essentials_tuple)
essentials_list.append(essential_item4)
essentials_tuple = tuple(essentials_list)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)