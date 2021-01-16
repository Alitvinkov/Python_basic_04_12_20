# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def prime_list(element_1, element_2):
    return element_1 * element_2

second_list = [element for element in range (100, 400, 100)]
print(second_list)
print(reduce(prime_list, second_list))