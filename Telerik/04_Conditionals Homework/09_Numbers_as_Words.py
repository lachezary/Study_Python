num1 = int(input())
hundreds = 0
tens = 0
ones = 0

if num1 // 100 > 0:
    hundreds = num1 // 100
if (num1 // 10) % 10 >= 0:
    tens = num1 // 10 % 10
ones = num1 % 10 

digit_hundreds = int(hundreds)
digit_tens = int(tens)
digit_ones = int(ones)

if hundreds == 1:
    hundreds = str("one hundred")
elif hundreds == 2:
    hundreds = str("two hundred")
elif hundreds == 3:
    hundreds = str("three hundred")
elif hundreds == 4:
    hundreds = str("four hundred")
elif hundreds == 5:
    hundreds = str("five hundred")
elif hundreds == 6:
    hundreds = str("six hundred")
elif hundreds == 7:
    hundreds = str("seven hundred")
elif hundreds == 8:
    hundreds = str("eight hundred")
elif hundreds == 9:
    hundreds = str("nine hundred")

if tens == 1:
    if ones == 0:
        tens = str("ten")
    elif ones == 1:
        tens = str("eleven")    
    elif ones == 2:
        tens = str("twelve")    
    elif ones == 3:
        tens = str("thirteen")   
    elif ones == 4:
        tens = str("fourteen")   
    elif ones == 5:
        tens = str("fifteen")   
    elif ones == 6:
        tens = str("sixteen")  
    elif ones == 7:
        tens = str("seventeen")
    elif ones == 8:
        tens = str("eightteen")
    elif ones == 9:
        tens = str("nineteen")
elif tens == 2:
    tens = str("twenty")
elif tens == 3:
    tens = str("thirty")
elif tens == 4:
    tens = str("fourty")
elif tens == 5:
    tens = str("fifty")
elif tens == 6:
    tens = str("sixty")
elif tens == 7:
    tens = str("seventy")
elif tens == 8:
    tens = str("eighty")
elif tens == 9:
    tens = str("ninety")
    
if tens != 1:
    if ones == 1:
        ones = str("one")
    elif ones == 2:
        ones = str("two")
    elif ones == 3:
        ones = str("three")
    elif ones == 4:
        ones = str("four")
    elif ones == 5:
        ones = str("five")
    elif ones == 6:
        ones = str("six")
    elif ones == 7:
        ones = str("seven")
    elif ones == 8:
        ones = str("eight")
    elif ones == 9:
        ones = str("nine")

result = ""

if digit_hundreds == 0 and digit_tens == 0 and digit_ones == 0:
    result = ("zero")
elif digit_hundreds > 0 and digit_tens > 0 and digit_tens != 1 and digit_ones > 0:
    result = hundreds + " and " + tens + " " + ones
elif digit_hundreds > 0 and digit_tens > 0 and digit_tens != 1 and digit_ones == 0:
    result = hundreds + " and " + tens   
elif digit_hundreds > 0 and digit_tens == 1:
    result = hundreds + " and " + tens
elif digit_hundreds > 0 and digit_tens == 0 and digit_ones > 0:
    result = hundreds + " and " + ones
elif digit_hundreds > 0 and digit_tens == 0 and digit_ones == 0:
    result = hundreds
elif digit_hundreds == 0 and digit_tens > 0 and digit_tens != 1 and digit_ones > 0:
    result = tens + " " + ones
elif digit_hundreds == 0 and digit_tens == 1:
    result = tens
elif digit_hundreds == 0 and digit_tens == 0 and digit_ones > 0:
    result = ones

print(result)