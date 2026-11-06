def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 2)


c = float(input("Температура в °C: "))
f = celsius_to_fahrenheit(c)
print(f"{c} °C = {f} °F")
