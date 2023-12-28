price_kg = float(input("Введите стоимость 1 кг конфет: "))
print("Стоимость конфет: ")
for kg in range(12, 21, 2):
    cost = kg * 0.1 * price_kg
    print(f"{kg * 0.1:.1f} kg: {cost:.2f}")