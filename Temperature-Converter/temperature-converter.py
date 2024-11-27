# Temperature converter

unit = input("Is this temperature in celcius or fahreinheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahreinheit is {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")