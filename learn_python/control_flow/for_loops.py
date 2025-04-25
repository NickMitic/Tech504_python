list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for num in list_data:
    print(2 * num)
print()
for data in embedded_lists:
    print(data)
    for num in data:
        print(num)
print()
for key in dict_data:
    print(key)
print()
for key in dict_data:
    print(dict_data[key])
print()
for key1 in dict_data:
    for key2 in dict_data[key1]:
        print(dict_data[key1][key2])
print()
for key in dict_data:
    print(dict_data[key]["money"])
print()
for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found 3")
    else:
        print("greater than 3")