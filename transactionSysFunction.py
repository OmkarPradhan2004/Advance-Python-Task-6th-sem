#Transaction system using Functions
id="Omkar.Pradhan_"
pin="2603"
attempt=0
maxattempt=3
login=False
while attempt < maxattempt:
    Uid=input("User:")
    Upass=input("Password:")
    if Uid==id and Upass==pin:
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
    def deposit(num,transaction):
        global balance
        balance+=num
        transaction.append("Deposited:"+str(num))
        print("Amount Deposited")

    def withdraw(num,transaction):
        global balance
        if num<=balance:
            balance-=num
            transaction.append("Withdraw: "+str(num))
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def history(transaction):
        print("Transaction History:")
        if len(transaction)==0:
            print("NO Transaction yet")
        else:
            for t in transaction:
                print(t)

    while True:
        print("\n1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.Transaction History")
        print("5.Exit")
        choice=int(input("Enter your choice:"))

        if choice==1:
            print("Deposit")
            amt=int(input("Enter Amount:"))
            deposit(amt,transaction)

        elif choice==2:
            print("Withdraw")
            amt = int(input("Enter Amount:"))
            withdraw(amt,transaction)

        elif choice==3:
            print("Current Balance:",balance)

        elif choice==4:
            history(transaction)
        
        elif choice==5:
            print("Thank You for using our Service")
            break

        else:
            print("Invalid Choice")