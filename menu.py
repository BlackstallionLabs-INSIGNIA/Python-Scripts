#! /usr/bin/env python3

import time
print ('By !NS!GN!A & Blackstallion Labs.')
print (29 * '-')
time.sleep(.1)
print ("   P R O G R A M - M E N U")
time.sleep(.1)
print (29 * '-')
time.sleep(.1)
print ("1. About")
time.sleep(.1)
print ("2. Monty Python Game")
time.sleep(.1)
print ("3. Addition Calculator")
time.sleep(.1)

print (29 * '-')

## Get the user's choice ###
choice = input('Enter your choice [1-3] : ')

### Change the string to an integer##
choice = int(choice)

### Select an option ###
if choice == 1:
        print('Loading...')
        time.sleep(.1)
        print(29 * '-')
        print('This menu script was designed by !NS!GN!A for Blackstallion labs. ' 
        'Each week, check my github repo for new scripts, whick will be added '
        'to this menu. Just redownload it and you are good to go!' ' If you use ' 
        'this script in any of your projects please DO NOT delete the `about` section.'
        ' It is the only way that I get credit for this script.' )
        print (29 * '-')
       
        
        

elif choice == 2:
        print('Starting Game...')
        time.sleep(.1)
        print(29 * '-')
        name = input("What is your name?")
        quest = input("What is your quest?")
        color = input("What is your favorite color?")
        
        print (29 * '-')
        print("So you mean to tell me that your name is %s, your quest is to %s, " \
        "and your favorite color is %s?" % (name, quest, color))
        print (29 * '-')
        

elif choice == 3:
        print ("Starting Calculator...")
        time.sleep(.1)
        print(29 * '-')
        num1 = input("Insert Number 1: ")
        num2 = input("Insert number 2: ")
        print (num2 + num1)
        print (29 * '-')
        
else:
        print ("Invalid number. Try again...")
        print (29 * '-')