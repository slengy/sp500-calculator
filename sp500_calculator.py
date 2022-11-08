sp500_return = 0.0767

try:
    investment = int(input('How much money will you invest now?: '))
    time_frame = int(input('How many years will you invest this money for?: '))
    monthly_contribution = int(input('How much money will you add each month?: '))
except ValueError:
    print('Error: please enter a number')

else:
    print(f'${investment}')
    print(f'{time_frame} years')
    print(f'${monthly_contribution}')

investment_return = investment*((1+(sp500_return/12))**(time_frame*12))
monthly_return = monthly_contribution*((((1+(sp500_return/12))**(time_frame*12))-1)/(sp500_return/12))
total_return = investment_return + monthly_return
print(f'In {time_frame} years you will have ${investment_return:,.2f} from your initial investment')
print(f'In {time_frame} years you will have ${monthly_return:,.2f} from your monthly investments')
print(f'In {time_frame} years you will have ${total_return:,.2f} total due to compounding')
