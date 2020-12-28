''' Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''

# вариант №1
def user_data(**user_strings):
    return user_strings.values()

first, last, your, city, email, phone = (user_data(
    first = input('Enter your name: '),
    last = input('Enter your last name: '),
    your = input('Enter your year of birth: '),
    city = input('Enter the city where you live: '),
    email = input('Enter your email address: '),
    phone = input('Enter your phone number: ')
    )
)
print(first, last, your, city, email, phone)

# вариант №2
def user_data(*user_list):
    for i in user_list:
        print(i, end=' ')

argument = []

first = input('Enter your name: ')
last = input('Enter your last name: ')
your = input('Enter your year of birth: ')
city = input('Enter the city where you live: ')
email = input('Enter your email address: ')
phone = input('Enter your phone number: ')

argument.extend((first, last, your, city, email, phone))

user_data(*argument)
print()
