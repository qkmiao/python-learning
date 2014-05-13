#!/usr/bin/python

number = 100
flag = 1

while flag:
    guess = int(raw_input("Please enter a number:"))

    if guess == 100:
        flag = 0
        print 'Right'
    elif guess > 100:
        print 'Wrong, please input a small number'
    else:
        print 'Wrong, please input a big number'
print 'DONE'
