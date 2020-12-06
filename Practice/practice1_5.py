user_proceed = input('Vvedite summu viruchki:\n>>> ')
user_spending = input('Vvedite summu izdergek:\n>>> ')

if user_proceed.isdigit() and user_spending.isdigit():
    user_proceed = int(user_proceed)
    user_spending = int(user_spending)
else:
    print('Vvesti chislovoe znachenie')
    exit()


if user_proceed > user_spending:
    profit = (user_proceed - user_spending)
    rentability = ((profit / user_proceed) * 100)

    personal = int(input('Vvedite chislo sotrudnikov: \n>>>'))
    personal_profit = (profit / personal)

    profit_info = f'Pribil sostavila:>>> {profit} \nPribil na sotrudnika: >>> {personal_profit}  '
    rentability_info = f'Rentabelnost:>>> {rentability} %'

    print(profit_info)
    print(rentability_info)
else:
    print('Ubitok')
    exit()
