# lesson 5: while loop
food = input("Enter food that you like? (q to quit): ")
while not food == "q" :
    print(f"you like {food}")
    food = input("Enter another food that you like? (q to quit): ")
print("Thanks for sharing your favorite foods!")