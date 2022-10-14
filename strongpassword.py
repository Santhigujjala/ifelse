passward=(input("enter your passward:"))
m=len(passward)
if m>=6 and m<=9:
    if "!"or"@"or"#"or"+"in passward:
        if passward>="a"or passward<="z":
            if passward>="A"or passward<="Z":
                    print("storng passward")
            else:
                print("enter the uppercase letters ")
        else:
            print("enter the lowercase letters")
    else:
        print("enter the special characters")
else:
    print("weak passward")        