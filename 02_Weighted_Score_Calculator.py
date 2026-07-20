#Weighted Score Calculator
name = input ("Enter your full name : ")
GAT =  float(input("Enter your GAT score : "))
SAAT = float(input("Enter your SAAT score : "))
shcool = float(input ("Enter your school grade : "))
reault = ((GAT*30)+(SAAT*30)+(shcool*40))/100
print(f"Your name is {name}")
print(f"Your GAT score is {GAT}")
print(f"Your SAAT score is {SAAT}") 
print(f"Your shcool score is {shcool}")
print(f"Your Weighted Score is {reault}")