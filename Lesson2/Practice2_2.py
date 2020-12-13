# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list = 0
i = 0

while True:
    list = input('Vvedite kolichestvo elementov v spiske:\n>>>')
    if list.isdigit():
        list = int(list)
        break
    else:
        print('Ne verno. Vvedite celoe chislo')

new_list1 = []
while i < list:
    new_list1.append(input(f'vvedite znachenie "{i}" elementa spiska: \n>>>'))
    i += 1
print(new_list1)

i = 0
while i <= list - 2:
    new_list1[i], new_list1[i + 1] = new_list1[i + 1], new_list1[i]
    i += 2
    print(new_list1)