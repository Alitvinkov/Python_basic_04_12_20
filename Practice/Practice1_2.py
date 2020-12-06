user_second = input('Vvedite vremya v sekundah: ')

if user_second.isdigit():
    user_second = int(user_second)
else:
    print('Vvesti chislovoe znachenie')
    exit()

var_minute = 60
secund_result = user_second
minute_result = (user_second // var_minute)
hour_result = (minute_result / 60)

total_result = f' \n<{secund_result} Sekund  \n<< {hour_result} : {minute_result} : {secund_result}'
print(total_result)
#print(minute_result)
#print(hour_result)
