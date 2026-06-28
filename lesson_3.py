weight=float(input("Enter the weight : "))
unit = input("Kilograms or pounds ? (K/L) ")
if unit == "K" :
    weight *= 2.205
    unit = "Las."
    print(f"your whight is {round(weight,1)} {unit}")
elif unit == "L" :
    weight/=2.205
    unit = "Kgs."
    print(f"your whight is {round(weight,1)} {unit}")
else :
    print(f"{unit} was not vaild")

