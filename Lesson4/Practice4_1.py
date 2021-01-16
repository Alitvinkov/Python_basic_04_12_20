# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def gehalt ():
    try:
        zeit, lohn, premie = map(float, argv[1:])
        print(f'gehalt - {zeit * lohn + premie}')
    except ValueError:
        print('Vvedite tri chisla. ')

gehalt()


