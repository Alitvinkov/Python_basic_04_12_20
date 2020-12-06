user_name = input('Vvedite vawe imya:\n>>>')
user_age = input('Vvedite vaw vozrast: \n>>>')

if user_age.isdigit():
    user_age = int(user_age)
else:
    print(user_name, 'Owibka vvoda: vvedite chislo')
    exit()

print('Dobriy vecher', user_name, '!')

sys_message = f'Polzovatel {user_name} \nv vozraste {user_age} \nvowel v sistemu'
print(sys_message)

if user_age >= 18:
    print('Dostup razreshen v XXX')
elif user_age >= 16:
    print('Dostup k boevikam')
else:
    print('Dostup ogranichen')

print('Otschet vozrasta')

temp_age = user_age
while temp_age > 0:
    if not temp_age & 1:
        temp_age -= 1
        continue
    print(temp_age)

    if temp_age == 15:
        break
    # temp_age = temp_age - 1
    temp_age -= 1
else:
    print('srabotal else cikla')
