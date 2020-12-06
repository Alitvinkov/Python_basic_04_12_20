user_scale = input('Vvedite chislo chislo bolwee 10: ')

if user_scale.isdigit():
    user_scale = int(user_scale)
else:
    print('Vvedite chislo')
    exit()

max_scale = user_scale % 10
x_scale = user_scale // 10


while x_scale > 0:
    if  x_scale % 10 > max_scale:
        max_scale  = x_scale % 10
    x_scale = x_scale // 10
print(max_scale)

#REwenie nawel v internete i spisal ya prosto ne do dumalsa do etogo reweniya (((