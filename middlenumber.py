a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a<c:
    print("a is second largest number")
elif b>a and b<c:
    print("b is second largest number")
elif c>a and c<b:
    print("c is second largest number")
else:
    print("second not largest number")