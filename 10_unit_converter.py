# Python Unit Converter
print(80*"#")
print(" You can Write the frist letter or full Name of unit Time ".center(80,"#"))
print(80*"#")
age = int(input("Enter your age : "))

unit = input("Enter your unit : months or Weeks or days : ").strip().lower()

months = age*12
weeks = months*4
days = age*365

if unit == "months" or unit == "m".strip().lower():
    print("you choose month")
    print(f"you Live for {months:,} months.")

elif unit == "weeks" or unit == "w".strip().lower():
    print("You choose Weeks")
    print(f"you Live for {weeks:,} Weeks.")
elif unit == "days"or unit == "d".strip().lower():
    print("You choose Days")
    print(f"You Live for {days:,} days.")
else:
    print("you choose wrong unit")


