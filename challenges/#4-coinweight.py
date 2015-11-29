#!/usr/bin/python
#
# Coding challenge #4 - Coin rolling by weight

# 1 gram = .002 pounds

# Individual coin weights by grams
centw = 2.5
nickw = 5.0
dimewt = 2.3
quarwt = 5.7

# Number of coins per wrapper
centwrp = 50
nickwrp = 40
dimewrp = 50
quarwrp = 40

# Weight of coins per wrapper in grams
centrollwt = centw * centwrp
nickrollwt = nickw * nickwrp
dimerollwt = dimewt * dimewrp
quarrollwt = quarwt * quarwrp

# Weight of coins per wrapper in pounds
crollwtp = centrollwt * 0.002
nrollwtp = nickrollwt * 0.002
drollwtp = dimerollwt * 0.002
qrollwtp = quarrollwt * 0.002


while True:
    print('Would you like to enter the weight of your coins in grams or pounds?')
    gorp = input('> ')
    if gorp.lower() == 'grams':
        print()
        print('Enter weight of pennies:')
        centin = float(input('> '))
        print('You have $' + str(round((centin / centw) * .01, 2)) + ' in pennies.')
        print()
        print('Enter weight of nickels:')
        nickin = float(input('> '))
        print('You have $' + str(round((nickin / nickw) * .05, 2)) + ' in nickels.')
        print()
        print('Enter weight of dimes:')
        dimein = float(input('> '))
        print('You have $' + str(round((dimein / dimewt) * .10, 2)) + ' in dimes.')
        print()
        print('Enter weight of quarters:')
        quarin = float(input('> '))
        print('You have $' + str(round((quarin / quarwt) * .25, 2)) + ' in quarters.')
        print()
        centrolls = int(centin / centrollwt)
        nickrolls = int(nickin / nickrollwt)
        dimerolls = int(dimein / dimerollwt)
        quarrolls = int(quarin / quarrollwt)
        break
    elif gorp.lower() == 'pounds':
        print()
        print('Enter weight of pennies:')
        centin = float(input('> '))
        print()
        print('Enter weight of nickels:')
        nickin = float(input('> '))
        print()
        print('Enter weight of dimes:')
        dimein = float(input('> '))
        print()
        print('Enter weight of quarters:')
        quarin = float(input('> '))
        print()
        centrolls = int(centin / crollwtp)
        nickrolls = int(nickin / nrollwtp)
        dimerolls = int(dimein / drollwtp)
        quarrolls = int(quarin / qrollwtp)
        break
    else:
        print('Please enter either \'grams\' or \'pounds\'.')
    

    
if centrolls == 0:
    print('You do not have enough pennies to fill an entire roll.')
elif centrolls == 1:
    print('You need ' + str(centrolls) + ' penny roll.')
else:
    print('You need ' + str(centrolls) + ' penny rolls.')
    

if nickrolls == 0:
    print('You do not have enough nickels to fill an entire roll.')
elif nickrolls == 1:
    print('You need ' + str(nickrolls) + ' nickel roll.')
else:
    print('You need ' + str(nickrolls) + ' nickel rolls.')


if dimerolls == 0:
    print('You do not have enough dimes to fill an entire roll.')
elif dimerolls == 1:
    print('You need ' + str(dimerolls) + ' dime roll.')
else:
    print('You need ' + str(dimerolls) + ' dime rolls.')

if quarrolls == 0:
    print('You do not have enough quarters to fill an entire roll.')
elif quarrolls == 1:
    print('You need ' + str(quarrolls) + ' quarter roll.')
else:
    print('You need ' + str(quarrolls) + ' quarter rolls.')






        

                  
        
        
        
        
