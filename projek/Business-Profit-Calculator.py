def calcPercent(h1,h2):
    percent = ((sale-cost)/cost)*100
    percent = round(percent, 2)
    if percent > 0:
        print(f'Your profits are {percent}%')
    else:
        print(f'Your Losses are {abs(percent)}%')


cost = float(input('cost (RM): '))
sale = float(input('sale (RM): '))

if cost == sale:
    print('No profit')
else:
    calcPercent(cost,sale
