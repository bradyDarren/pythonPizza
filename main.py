print("Welcome to Python Pizza Delivery")
size = input("What size pizza would you like to order? S, M, L: ").lower()
pepperoni = input("Would you like pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Would you like to add extra cheese? Y or N: ").lower()

total_cost = 0

if size == "s":
    total_cost += 15
elif size == "m":
    total_cost += 20
elif size == "l":
    total_cost += 25

if pepperoni == "y":
    if size == "s":
        total_cost += 2
    elif size == "l" or "m":
        total_cost += 3

if extra_cheese == "y":
    total_cost += 1


print(f"The total cost of your pizza is: ${total_cost}")
