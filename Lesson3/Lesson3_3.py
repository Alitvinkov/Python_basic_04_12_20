# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

count_1 = int(input('Vvedite chislo X: \n >>>>'))
count_2 = int(input('Vvedite chislo Y: \n >>>>'))
count_3 = int(input('Vvedite chislo Z: \n >>>>'))


def func():
    if count_2 < count_1 < count_3:
        final_count = count_1 + count_3
    elif count_1 < count_2 < count_3:
        final_count = count_2 + count_3
    elif count_3 < count_1 and count_3 < count_2:
        final_count = count_2 + count_1
    return final_count

print(func())
