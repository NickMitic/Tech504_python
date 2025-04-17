starters = ["soup", "salad","tart"]
mains = ["pasta","steak","fish"]
desserts = ["ice cream","cake","cheese"]
starters_order = []
mains_order = []
desserts_order = []
prices = {"soup":4,"salad":6,"tart":7,
          "pasta":10,"steak":15,"fish":20,
          "ice cream":3,"cake":5,"cheese":7}

customers = 0
while customers < 1:
    customers = int(input("Hello, how many people are eating today? "))

print(f"Our starters today are {starters[0]}, {starters[1]} and {starters[2]}")
for i in range(1,customers+1):
    starter = ""
    while starter not in starters:
        starter = input(f"Customer {i}, what will you have to start? ").lower()
    starters_order.append(starter)

print(f"Our mains are {mains[0]}, {mains[1]} and {mains[2]}")
for i in range(1,customers+1):
    main = ""
    while main not in mains:
        main = input(f"Customer {i}, what will you have for your main? ").lower()
    mains_order.append(main)

print(f"And our desserts are {desserts[0]}, {desserts[1]} and {desserts[2]}")
for i in range(1,customers+1):
    dessert = ""
    while dessert not in desserts:
        dessert = input(f"Customer {i}, which dessert would you like? ").lower()
    desserts_order.append(dessert)

order_dict = {"soup":starters_order.count("soup"),"salad":starters_order.count("salad"),"tart":starters_order.count("tart"),
          "pasta":mains_order.count("pasta"),"steak":mains_order.count("steak"),"fish":mains_order.count("fish"),
          "ice cream":desserts_order.count("ice cream"),"cake":desserts_order.count("cake"),"cheese":desserts_order.count("cheese")}

bill = sum([list(prices.values())[i] * list(order_dict.values())[i] for i in range(9)])

print(f"Thank you, that will be £{bill} please.")


