import pricelist as p
import smithing

print('mithril efficiency')



#base prices
print('prices are active as of ' + p.gedate)
print('mithril bar price: ' + str(p.mithrilbar))
print('mithril ore price: ' + str(p.mithrilore))
print('coal price: ' + str(p.coal))

#efficiency of bars

#mithril bar recipe 4 coal, 1 mithril
smeltprice = p.mithrilore + p.coal * 4
print('****' * 8)
print('price to smelt: ' + str(smeltprice))
print('profit to smelt: ' + str(p.mithrilbar - smeltprice))

#things to do with bars
smithing.smithefficiency('mithril', p.mithrilbar)

