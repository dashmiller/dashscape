import pricelist as p
#healing per gp

print('this script tells you the healing provided per gp')
print('of course, this does not consider slot efficiency. that is up to you.')

#heal amounts
tunaheal = 750
lobsterheal = 1200
sfheal = 1400
monkheal = 1600
sharkheal = 2000

foods = ['tuna','lobster','swordfish','monkfish','shark']

def getfoodprice(food):
    if food == 'tuna':
        return p.tuna
    elif food == 'lobster':
        return p.lobster
    elif food == 'swordfish':
        return p.swordfish
    elif food == 'monkfish':
        return p.monkfish
    elif food == 'shark':
        return p.shark

def getheal(food):
    if food == 'tuna':
        return tunaheal
    elif food == 'lobster':
        return lobsterheal
    elif food == 'swordfish':
        return sfheal
    elif food == 'monkfish':
        return monkheal
    elif food == 'shark':
        return sharkheal

tunabaseline = p.tuna / tunaheal

print('tuna heals ' + str(tunaheal) + ' and costs ' + str(p.tuna))

for food in foods:
    foodprice = getfoodprice(food)
    healvalue = getheal(food)
    cetuna = (foodprice / healvalue) / tunabaseline
    hetuna = (healvalue / tunaheal)
    print(food + ' costs ' + str(cetuna) + ' as much as tuna and heals ' + str(hetuna) + ' more than tuna')
