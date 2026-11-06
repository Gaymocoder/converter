def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 2)


try:
    c = float(input("Температура в °C: ").replace(",", "."))
except ValueError:
    print("Нужно ввести число")
    raise SystemExit(1)

f = celsius_to_fahrenheit(c)
print(f"{c} °C = {f} °F")
