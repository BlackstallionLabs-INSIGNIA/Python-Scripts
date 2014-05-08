#! /usr/bin/env python3
import time
print (25 * '-')
time.sleep(.1)
print ("   B O O T - M E N U")
time.sleep(.1)
print (25 * '-')
time.sleep(.1)
print ("1. About")
time.sleep(.1)
print ("2. Monty Python Game")
time.sleep(.1)
print ("3. Addition Calculator")
time.sleep(.1)

print (25 * '-')

## Get input ###
choice = input('Enter your choice [1-3] : ')

### Convert string to int type ##
choice = int(choice)

### Select an option ###
if choice == 1:
        print('Loading...')
        time.sleep(.1)
        print(25 * '-')
        print('This script was designed by !NS!GN!A for Blackstallion labs. ' 
        'Each week, check my github repo for new scripts, whick will be added '
        'to this menu. Just redownload it and you are good to go!')
        print (25 * '-')
       
        
        

elif choice == 2:
        print('Starting Game...')
        time.sleep(.1)
        print(25 * '-')
        name = input("What is your name?")
        quest = input("What is your quest?")
        color = input("What is your favorite color?")
        
        
        print("So you mean to tell me that your name is %s, your quest is to %s, " \
        "and your favorite color is %s?" % (name, quest, color))
        print (25 * '-')
        

elif choice == 3:
        print ("Starting Calculator...")
        time.sleep(.1)
        print(25 * '-')
        num1 = input("Insert Number 1: ")
        num2 = input("Insert number 2: ")
        print (num2 + num1)
        print (25 * '-')
        

else:
        print ("Invalid number. Try again...")
        print (25 * '-')