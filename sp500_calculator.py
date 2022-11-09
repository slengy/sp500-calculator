sp500_return = 0.0767

try:
    investment = int(input('How much money will you invest now?: $'))
    time_frame = int(input('How many years will you invest this money for?: '))
    monthly_contribution = int(input('How much money will you add each month?: $'))
except ValueError:
    print('Error: please enter a number')
    exit()
    
investment_return = investment*((1+(sp500_return/12))**(time_frame*12))
monthly_return = monthly_contribution*((((1+(sp500_return/12))**(time_frame*12))-1)/(sp500_return/12))
total_return = investment_return + monthly_return

print('')
print(f'In {time_frame} years you will have ${total_return:,.2f} total due to compound interest')
print('')
print(f'${investment_return:,.2f} is due to your initial ${investment:,.0f} investment')
print('')
print(f'${monthly_return:,.2f} is from your ${monthly_contribution:,.0f} monthly contribution')
print('')
