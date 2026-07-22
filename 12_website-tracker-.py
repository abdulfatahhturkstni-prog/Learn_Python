

myfavoritewebsites = []

maxwebsites = 5

while maxwebsites > 0:

    web = input("Enter a website without http:// or https:// : ")
    myfavoritewebsites.append(web.strip().lower())
    maxwebsites -= 1

    print(f"You have entered {len(myfavoritewebsites)} websites")
    print(myfavoritewebsites)

    

else :
    print("You have entered more than 5 websites")
    n=0
if len(myfavoritewebsites)>0:
    myfavoritewebsites.sort()
    print("Your favorite websites are:")
    while n < len(myfavoritewebsites):
        print(f"http://{myfavoritewebsites[n]}")
        n += 1