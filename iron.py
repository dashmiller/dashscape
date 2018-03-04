import pricelist as p

#this one is a little interesting because of the chance of failure at producing an iron bar

print('prices are active as of ' + p.gedate)

print('iron ore price: ' + str(p.ironore))
print('iron bar price: ' + str(p.ironbar))

prof100 = p.ironbar - p.ironore
prof80 = (p.ironbar * .80) - p.ironore

print('profit assuming 100%: ' + str(prof100))
print('profit assuming 80%: ' + str(prof80))
print('cost to use ring of forging : ' + str(p.ringofforging / 140))

if (p.ringofforging / 140) < (prof100 - prof80):
    print('ring of forging is efficient by: ' + str((p.ironbar - (p.ringofforging / 140)) - prof80))
else:
    print('ring of forging is not efficient')

