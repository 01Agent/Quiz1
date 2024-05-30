#!/usr/bin/env python3

print("1. Convert inches --> cm ")

print("2. Convert cm --> inches")

choice = input("Enter your choice (1,2):")

if choice == '1':
    inches= int(input("Enter the inches: "))
    cm = inches * 2.54
    print("Number of cm: " +str(cm))

elif choice == '2':
    cm = int(input("Enter cm: "))
    inches = cm / 2.54
    print("Nummber of inches:" +str(inches))

else:
    print("Invalid entry")