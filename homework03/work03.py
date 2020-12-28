''' Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''

def max_summ(a, b, c):
    x = [a, b, c]
    x.remove(min(a, b, c))
    return sum(x)
a, b, c = map(int, input('Введите 3 числа используя пробел: ') .split())
print(max_summ(a, b, c))
