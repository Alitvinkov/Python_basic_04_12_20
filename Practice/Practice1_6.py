run1_result = int(input('Ukagite kolichestvo kilometrov v 1 den: \n>>>'))
wish_run = int(input('Ukagite gelaemoe kolichestvo kilometrov kotoroe vi hotite probegat: \n>>>'))

day_run = 1
while run1_result < wish_run:
    run1_result *= 1.1
    day_run +=1
    print(f'Den No {day_run}  {run1_result}km')

print(day_run)




