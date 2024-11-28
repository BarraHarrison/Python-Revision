# Shopping cart program
# Import regular expressions for validation purposes
import re 

foods = {}
total = 0

# Regular expression to validate price (up to 2 decimal places)
price_pattern = r"^\d+(\.\d{1,2})?$"

while True:
    food = input("Enter a food to buy (Press q to quit): ")
    if food.lower() == "q":
        break
    else:
        while True:
            price_input = input(f"Enter the price of {food}: $")
            if re.match(price_pattern, price_input):
                price = float(price_input)
                foods[food] = price
                break
            else:
                print("Invalid price. Please enter a number up to 2 decimal places (eg., 10.99).")
                

print("----- YOUR CART -----")
for food, price in foods.items():
    print(f"{food}: ${price:.2f}")
    total += price

print(f"\nTotal: ${total:.2f}")