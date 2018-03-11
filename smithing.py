import pricelist as p

def smithefficiency(bartype, barprice):
    arrowhead = getarrowhead(bartype)
    dagger = getdagger(bartype)
    sword = getsword(bartype)
    scim = getscim(bartype)
    #if for some reason we dont have bartype/valid prices
    if not arrowhead:
        print('we dont have a bartype or valid price for bartype')
        return
    print('we have valid prices for ' + bartype)
    print('arrowhead : ' + str(arrowhead - (barprice / 15)))
    print('dagger: ' + str(dagger - barprice))
    print('sword: ' + str(sword - barprice))
    print('scimitar: ' + str (scim - (barprice * 2)))


def getarrowhead(bartype):
    if bartype == 'mithril':
        return p.mithrilarrowhead

def getdagger(bartype):
    if bartype == 'mithril':
        return p.mithrildagger

def getsword(bartype):
    if bartype == 'mithril':
        return p.mithrilsword

def getscim(bartype):
    if bartype == 'mithril':
        return p.mithrilscim