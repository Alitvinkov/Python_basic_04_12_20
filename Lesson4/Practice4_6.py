# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

print('Genereruem celie chisla\n Dlya vihoda -  "Q"\n Dlya sleduywego chisla - ENTER ')
for element in count(int(input('Vvedite startovoe chislo \n>>>>>>'))):
    print(element, end='')
    quit = input()
    if quit == 'q':
        break

print('Povtoryaem elementi spiska\n Dlya vihoda -  "Q"\n Dlya sleduywego chisla - ENTER')

list = input('Vvedite chisla cherez probel: \n>>>>>>').split()
list_it = cycle(list)
quit = None

while quit != 'q':
    print(next(list_it), end='')
    quit = input()
