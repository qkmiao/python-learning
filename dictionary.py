#!/usr/bin/python

dict = {'a' : 'apple',
        'b' : 'box',
        'c' : 'cat',
        'd' : 'dog'}

if 'a' in dict:
    print dict['a']

for letter, word in dict.items():
    print '%s is at the beginnig of %s' %(letter, word)

dict['e'] = 'egg'
dict.sort()
print dict
