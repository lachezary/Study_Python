# A phone bill plan includes 
# 1 hour of free calls and 
# 20 text messages for 12.00 levas. 
# Each 
# additional minute costs 0.10 levas and each 
# additional message costs 0.06 levas. 
# Also, any additional minutes/text messages are subject to 20% sales tax. 
# Write a program that calculates the additional charge for text, 
# the additional charge for minutes, and the sales tax charge for both. 
# Also, display the total amount paid.

# Input
# On the first line, you will receive the total amount of text messages.
# On the second line, you will receive the total amount of minutes.
# Output
# 1st line - number of additional messages and additional amount paid
# 2nd line - number of additional minutes and additional amount paid
# 3rd line - amount paid in taxes
# 4th line - total bill

messages_amount = int(input())
calls_minutes = int(input())
messages_cost = 0
additional_messages = 0
plan_cost = 12
tax = 0
call_cost = 0
additional_calls = 0
total = 0

if messages_amount > 20:
    additional_messages = messages_amount - 20
    messages_cost = float(0.06)
    messages_cost = additional_messages * messages_cost

if calls_minutes > 60:
    additional_calls = calls_minutes - 60
    call_cost = float(0.1)
    call_cost = additional_calls * call_cost

if messages_amount > 20 or calls_minutes > 60:
    tax = (call_cost + messages_cost) * 0.2

total = plan_cost + messages_cost + call_cost + tax

print(f"{additional_messages} additional messages for {messages_cost:.2f} levas")
print(f"{additional_calls} additional minutes for {call_cost:.2f} levas")
print(f"{tax:.2f} additional taxes")
print(f"{total:.2f} total bill")


