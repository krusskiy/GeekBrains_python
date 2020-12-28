''' Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. '''


def dividing(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "No / 0"
    except ValueError:
        return "No value"

print(dividing(int(input('Enter the first number: ')), int(input('Enter the second number: '))))
