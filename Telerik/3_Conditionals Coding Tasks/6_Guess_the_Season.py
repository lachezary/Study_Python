# Write a program that displays the name of the season associated with a given date and month. 
# Use the table below to determine the season's start and end dates.

# Season	Start Date
# Spring	March 20
# Summer	June 21
# Autumn	September 22
# Winter	December 21
# For example, Autumn lasts from September 22 to December 20, both inclusive.

# Input
# On the first line, you will receive the month as a string
# On the second line, you will receive the date as a number
# Output
# On the only line of output, print the name of the season in pascal case

month_input = input()
date_input = int(input())

if month_input == "April" or month_input == "May":
    print("Spring")
elif month_input == "July" or month_input == "August":
    print("Summer")
elif month_input == "October" or month_input == "November":
    print("Autumn")
elif month_input == "January" or month_input == "February":
    print("Winter")
elif month_input == "March" and date_input < 20:
    print("Winter")
elif month_input == "March" and date_input >= 20:
    print("Spring")
elif month_input == "June" and date_input < 21:
    print("Spring")
elif month_input == "June" and date_input >= 21:
    print("Summer")
elif month_input == "September" and date_input < 22:
    print("Summer")
elif month_input == "September" and date_input >= 22:
    print("Autumn")
elif month_input == "December" and date_input < 21:
    print("Autumn")
elif month_input == "December" and date_input >= 22:
    print("Winter")