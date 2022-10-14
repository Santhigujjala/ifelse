print("welcom to canara bank")
print("insert your card")
print("select your language")
language=input("enter the language")
if language=="english":
    amount=5000
    pin=int(input("enter the pin"))
    if pin==1234:
        print("transaction:1.withdraw 2.balance enquiry 3.pin_change 4.deposit 5.exit")
    transcation=int(input("enter the transaction"))
    if transcation==1:
        withdraw=int(input("enter the number amount+"))
        if withdraw<=amount:
            print("transaction succesful:","collect your withdraw cash") 
            print("remaing balance",amount+withdraw)
        else:
            print("not withdraw")
    if transcation==2:
        print("available balance is",amount)
        print("thank you")
    if transcation==3:
        pin_change=int(input("enter the new pin:"))
        if pin_change!=1234:  
            print("your new pin generation is successfully completed")
        else:
            print("your new pin generation is not completed")
    if transcation==4:
        deposit=int(input("enter the amount"))
        if deposit>=1000:
            print("your deposit anount is successfully completed,amount+deposite")
        else:
            print("not deposite")
    if transcation==5:
        print("exit")