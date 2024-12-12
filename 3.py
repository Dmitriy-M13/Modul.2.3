cost = float(input("Введите стоимость разговора: "))
print("Выберите оператор:")
print("1. МТС")
print("2. Билайн")
print("3. Мегафон")
operator = int(input("Введите номер оператора: "))

if operator == 1:
    total_cost = cost * 1.2
elif operator == 2:
    total_cost = cost * 1.1
elif operator == 3:
    total_cost = cost * 1.3
else:
    print("Некорректный номер оператора")

print("Итоговая стоимость разговора:", total_cost)