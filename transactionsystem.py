id="Omkar.Pradhan_"
pin="2603"
attempt=0
maxattempt=3
login=False
while attempt<maxattempt:
    in_id=input("User:")
    in_pass=input("Password:")
    if in_id==id and in_pass==pin:
        print("Login Successful!")
        login=True
        break

    else:
        print("Invalid Credentials!")
        print("Try Again!")
        attempt+=1

if login==True:
    balance=0
    transaction=[]
    while True:
        print("\n1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.Transaction History")
        print("5.Exit")

        choice=int(input("Enter your choice:"))
        if choice==1:
            amt=int(input("Enter Deposit Amount:"))
            balance+=amt
            transaction.append("Deposited:"+str(amt))
            print("Amount Deposited")

        elif choice==2:
            amt=int(input("Enter Withdraw Amount:"))
            if amt<+balance:
                balance-=amt
                transaction.append("withdraw:"+str(amt))
            else:
                print("Insufficient Balance")

        elif choice==3:
            print("Current Balance:",balance)

        elif choice==4:
            print("Transaction History:")
            if len(transaction)==0:
                print("NO Transaction yet")
            else:
                for t in transaction:
                    print(t)
        
        elif choice==5:
            print("Thank You for using our Service")
            break

        else:
            print("Invalid Choice")