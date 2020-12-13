# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
year_list = ['Zima', 'Vesna', 'Leto', 'Osen']
year_dict = {
    0: 'Zima',
    1: 'Vesna',
    2: 'Leto',
    3: 'Osen',
}
month = ()

while True:
    month = input('Vvedite nomer mesyaca v vide celogo chisla ot 1 - 12 :\n>>>')
    if month.isdigit():
        month = int(month)
        break
    else:
        print('Vi vveli neverni format')
month = 0 if month == 12 else month

print('Po spisku: ' + year_list[month // 3])
print('Po slovaru: ' + year_dict.get(month // 3))
