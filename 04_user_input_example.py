# variables enter user input example
username = input("Enter your username : ")

if 12>len(username):
    print("username must be more than 12 characters")
elif not username.find(" ")==-1:
        print("username must not contain space")    
elif not username.isalpha():    
    print("username must contain only numbers and alphabets")
else:
    print(F"username is {username}")