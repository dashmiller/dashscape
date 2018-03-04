print('mithril efficiency')

#TODO grab prices automatically

#variables
mithrilbar = 1567
mithrilore = 403
coal = 141
gedate = 'mar 4 2018'


#base prices
print('prices are active as of ' + gedate)
print('mithril bar price: ' + str(mithrilbar))
print('mithril ore price: ' + str(mithrilore))
print('coal price: ' + str(coal))

#efficiency of bars

#mithril bar recipe 4 coal, 1 mithril
smeltprice = mithrilore + coal * 4
print('****' * 8)
print('price to smelt: ' + str(smeltprice))
print('profit to smelt: ' + str(mithrilbar - smeltprice))
