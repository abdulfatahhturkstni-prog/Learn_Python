# Python compound interest calculator
principal =0
rate = 0
time = 0

while  True :
    principal = float(input("Enter principal amount: "))
    if principal <=0 :
        print("principal amount must be greater than 0")
    else :
        break
while True : 
    rate = float(input("Enter interest rate: "))
    if rate <=0 :
        print("interest rate must be greater than 0")
    else :
        break
while True : 
    time = float(input("Enter time period: "))
    if time <=0 :
      print("time period must be greater than 0")
    else : 
     break
result = principal * pow(1+rate/100, time)

print(f" balance after {time} years is ${result:.2f}")