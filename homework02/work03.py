''' Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict. '''

# Вариант через list, dict
number = int(input('Выберите месяц от 1 до 12: '))
if 0 < number <=12 :
    month_dict = {1: 'Зима',
                  2: 'Зима',
                  3: 'Весна',
                  4: 'Весна',
                  5: 'Весна',
                  6: 'Лето',
                  7: 'Лето',
                  8: 'Лето',
                  9: 'Осень',
                  10: 'Осень',
                  11: 'Осень',
                  12: 'Зима'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f'\nРеализация через list: {month_list[i]}')
            break
    print(f'Реализация через dict: {month_dict[number]}')
else:
    print('Вы сделали ошибку')

# Вариант через dict
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input('\nВыберите месяц от 1 до 12: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
