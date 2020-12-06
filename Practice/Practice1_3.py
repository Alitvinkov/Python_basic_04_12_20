user_scale = input('Vvedite chislo ot 1 do 9: ')

if user_scale.isdigit():
    user_scale = int(user_scale)
else:
    print('Vvesti chislovoe znachenie')
    exit()
# if user_scale > 9 and user_sacale :
# print('ne korrektnoe chislo')
# exit()

user_temp = user_scale
while 0 < user_temp <= 9:
    print(user_temp)
    break
else:
    print('Ne korrektnoe chislo')
    exit()
user_scale1 = user_scale * 11
user_scale2 = user_scale * 111
user_scale3 = (user_scale + user_scale1 + user_scale2)
user_result = f'{user_scale} + {user_scale1} + {user_scale2} = {user_scale3}'

print(user_result)
