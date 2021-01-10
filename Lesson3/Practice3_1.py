# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def count(a, b):
    if a == 0:
        print('ne verno')
    return a / b


x = int(input('VVedite chislo X'))
y = int(input('Vvedite chislo Y'))
result = count(x, y)
print(result)
