#!/usr/bin/python
#
# Coding challenge - Coin Denomination Change Maker

pennies = 0
nickels = 0
dimes = 0
quarters = 0

while True:
    print('Enter item price (Q to  quit):')
    item_cost = input('> ')
    if item_cost.lower() == 'q':
        break
    try:
        item_cost = float(item_cost)
    except ValueError:
        print('Value entered must be a dollar amount (Ex: 3.52)')
        print()
        continue
    print()
    print('Enter amount tendered:')
    amt_tend = float(input('> '))
    chg_amt = amt_tend - item_cost
    print()
    print('The change is $' + str(round(chg_amt, 2)) + '.')

    if chg_amt > 0.99:
        dollars = int(chg_amt)
        chg_amt = round(chg_amt - dollars, 2)
        chg_amt *= 100

    while chg_amt > 25:
        chg_amt -= 25
        quarters += 1

    while chg_amt > 10:
        chg_amt -= 10
        dimes  += 1
        
    while chg_amt > 5:
        chg_amt -= 5
        nickels += 1

    while chg_amt > 0:
        chg_amt -= 1
        pennies += 1
        
    print()
    print('Change denominations:')
    print()
    print('Dollars: ' + str(dollars))
    print('Quarters: ' + str(quarters))
    print('Dimes: ' +  str(dimes))
    print('Nickels: ' + str(nickels))
    print('Pennies: ' + str(pennies))
    print()
    
