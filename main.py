# Запрос чисел у пользователя
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Выбор операции
operation = input("Введите операцию (+, -): ")

# Вычисление результата
if operation == "+":
  result = a + b
elif operation == "-":
  result = a - b
else:
  result = "Неверная операция!"

print("Результат:", result)
