# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
max_number = -1

while number > 10:
    d = number % 10 # Получаем крайнюю цифру number
    number //= 10 # Обрезаем последнюю цифру number

    if d > max_number:
        max_number = d
print(max_number)
