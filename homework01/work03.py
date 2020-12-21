# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input('\nВведите число: '))
n = str(number)
n1 = n + n
n2 = n + n + n
summ = number + int(n1) + int(n2)
print (f'Сумма чисел "n + nn + nnn" равна: {summ}\n')
