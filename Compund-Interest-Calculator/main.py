# Compound Interest Calculator
# Interest is a charge for borrowing money, in case you need the definition of "interest"

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the interest rate amount: "))
    if rate < 0:
        print("The interest rate cannot be less than 0")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("The time cannot be less 0")
    else:
        break

# Formula used to calculate compound interest
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
