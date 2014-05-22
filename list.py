#!/usr/bin/python

shoplist = ['apple', 'origin', 'water']
print 'I have', len(shoplist), 'to buy'
for item in shoplist:
    print item

print 'I also have to buy rice.'
shoplist.append('rice')
print 'Now I need to buy these items:', shoplist
shoplist.sort()
print 'Items after sorted are:', shoplist

del shoplist[0]
print 'After buy first item, now shopping list is:', shoplist
