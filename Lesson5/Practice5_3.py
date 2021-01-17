# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


personal_count = 0
salary_count = 0

with open('Practice5_3.txt', 'r') as file:
    print('Oklad menwe 20000: ')
    for line in file:
        personal_count += 1
        personal = line.split()
        salary_count += int(personal[1])
        if int(personal[1]) < 20000:
            print(personal[0])
print(f'Srednya ZP vseh sotrudnikov: {salary_count / personal_count:.2f} ')


