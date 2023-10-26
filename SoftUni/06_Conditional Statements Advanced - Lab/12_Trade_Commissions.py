city_input = input()
sales_input = float(input())
commission = 0

if sales_input < 0:
    print("error")

if city_input == "Sofia":
    if sales_input >= 0 and sales_input <= 500:
        commission = sales_input * 0.05
        print(f"{commission:.2f}")
    elif sales_input > 500 and sales_input <=1000:
        commission = sales_input * 0.07
        print(f"{commission:.2f}")        
    elif sales_input > 1000 and sales_input <=10000:
        commission = sales_input * 0.08
        print(f"{commission:.2f}")   
    elif sales_input > 10000:
        commission = sales_input * 0.12
        print(f"{commission:.2f}")
elif city_input == "Varna":
    if sales_input >= 0 and sales_input <= 500:
        commission = sales_input * 0.045
        print(f"{commission:.2f}")
    elif sales_input > 500 and sales_input <=1000:
        commission = sales_input * 0.075
        print(f"{commission:.2f}")        
    elif sales_input > 1000 and sales_input <=10000:
        commission = sales_input * 0.10
        print(f"{commission:.2f}")   
    elif sales_input > 10000:
        commission = sales_input * 0.13
        print(f"{commission:.2f}")
elif city_input == "Plovdiv":
    if sales_input >= 0 and sales_input <= 500:
        commission = sales_input * 0.055
        print(f"{commission:.2f}")
    elif sales_input > 500 and sales_input <=1000:
        commission = sales_input * 0.08
        print(f"{commission:.2f}")        
    elif sales_input > 1000 and sales_input <=10000:
        commission = sales_input * 0.12
        print(f"{commission:.2f}")   
    elif sales_input > 10000:
        commission = sales_input * 0.145
        print(f"{commission:.2f}")
else:
    print("error")