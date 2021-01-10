# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def count_ask ():
    name = input('Vvedite Vawe imya:\n>>>>')
    sur_name = input('Vvedite vawu familiyu: \n>>>>')
    birth_date = input('Ukajite vaw god rogdeniya v formate dd.mm.yy: \n>>>>')
    city = input('Vaw gorod projivaniya: \n>>>>')
    email = input('Vvedite vaw email: \n>>>>')
    handy_nummer = input('Vvedite vaw nomer telefona: \n>>>>')
    info = print(f'Polzovatel {name} {sur_name} {birth_date} projivayuwii v gorode {city} kontaktnie dannie {email}')
    return info
count_ask()