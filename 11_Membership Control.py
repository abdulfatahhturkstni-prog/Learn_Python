# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------
#List if admins
admins = ["Abdulfattah","Mohmmed","Abdullah","Ahmed"]

# Login
name = input("please enter your Name: ").strip().capitalize()
# if name is in admins list
if name in admins:
    print(f"Welcome {name} to the administration panel")
    option = input("Please enter your option (update or delete): ").strip().lower()
    # update option
    if option == "update" or option == "u":
        new_name = input("Please enter your new name: ").strip().capitalize()
        admins[admins.index(name)] = new_name
        print(f"This is the new list after updating {name} to {new_name}")
        print(admins)
    # delete option
    elif option == "delete" or option == "d" :
        print(f"You have deleted {name} from the administration panel")
        admins.remove(name)
        print(f"This is the list after deleting {name}")
        print(admins)
    else: ## Wrong Option
        print("Invalid option selected.")

else: 
   status = input("your not admin, do you want to be an admin? (y/n)").strip().lower()
   if status == "y" or status=="Yes":
       admins.append(name)
       print(f"{name} you are now an admin")
       print(admins)  

   else:
       print("You Are not Add , good bye")


       

