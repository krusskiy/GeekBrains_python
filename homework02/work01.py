'''Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.'''

array = [1, 'Moscow', True, 2, 33, 5, '55']
for i in array:
    print(type(i))