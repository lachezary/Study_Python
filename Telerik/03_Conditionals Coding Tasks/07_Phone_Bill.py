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


