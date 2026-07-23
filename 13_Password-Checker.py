name= input("Enter your name : ")
mainpassword = "Abdulfatah1@"
password = input("Enter your password : ").strip()
try_count =4 

while password != mainpassword:
    try_count -= 1
    print(f"Wrong password, You have {"\"Last time\" " if try_count==0 else try_count}) ")
    password = input("Enter your password : ")
    

    if try_count == 0:
        print("You have no tries left")
        break


else:
    print(f"Welcome {name}\nYou Passsword is correct")