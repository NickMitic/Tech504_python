print("Hello")
print(["starter1","starter2","starter3"])
starter = input("Starter? ")
print(["main1","main2","main3"])
main = input("Main? ")
print(["dessert1","dessert2","dessert3"])
dessert = input("Dessert? ")
meal = [starter,main,dessert]
print(f"So your meal will be {meal[0]}, {meal[1]} and {meal[2]}")

prices = {"starter1":1,"starter2":2,"starter3":3,
          "main1":10,"main2":15,"main3":20,
          "dessert1":3,"dessert2":5,"dessert3":7}
bill = prices[starter] + prices[main] + prices[dessert]
print(bill)