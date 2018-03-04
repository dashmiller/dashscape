import pricelist as p
#healing per gp

print('this script tells you the healing provided per gp')
print('of course, this does not consider slot efficiency. that is up to you.')

#heal amounts
tunaheal = 750
lobsterheal = 1200
sfheal = 1400

foods = ['tuna','lobster','swordfish']

def getfoodprice(food):
    if food == 'tuna':
        return p.tuna
    elif food == 'lobster':
        return p.lobster
    elif food == 'swordfish':
        return p.swordfish

def getheal(food):
    if food == 'tuna':
        return tunaheal
    elif food == 'lobster':
        return lobsterheal
    elif food == 'swordfish':
        return sfheal

tunabaseline = p.tuna / tunaheal

print('tuna heals ' + str(tunaheal) + ' and costs ' + str(p.tuna))

for food in foods:
    foodprice = getfoodprice(food)
    healvalue = getheal(food)
    cetuna = (foodprice / healvalue) / tunabaseline
    hetuna = (healvalue / tunaheal)
    print(food + ' costs ' + str(cetuna) + ' as much as tuna and heals ' + str(hetuna) + ' more than tuna')