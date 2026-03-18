def deposit(account,amount):
    account['balance']+=amount
    account['history'].append(f"Deposited:{amount}")
    print(f"Deposited:{amount}.Balance:{account['balance']}")

def withdraw(account,amount):
    if amount<=account['balance']:
        account['balance']-=amount
        account['history'].append(f"Withdrew:{amount}")
        print(f"Success.Balance:{account['balance']}")
    else:
        print("Insufficient Balance!")

def show_history(account,username):
    print(f"\nHistory for {username}:")
    if not account['history']:
        print("No transactions.")
    else:
        for t in account['history']:print(f"- {t}")

def atm_menu(account,username):
    while True:
        print(f"\nWelcome,{username}\n1.Deposit\n2.Withdraw\n3.Balance\n4.History\n5.Logout")
        try:
            choice=int(input("Choice:"))
        except ValueError:
            continue

        if choice==1:
            deposit(account,int(input("Amt:")))
        elif choice==2:
            withdraw(account,int(input("Amt:")))
        elif choice==3:
            print(f"Balance:{account['balance']}")
        elif choice==4:
            show_history(account,username)
        elif choice==5:
            break
        else:
            print("Invalid")

def main():
    accounts={
        "Omkar.Pradhan_":{"pin":"2603","balance":0,"history":[]},
        "Chiranjeebi.Samal_":{"pin":"1234","balance":0,"history":[]},
    }
    print("ATM System")
    att,max_att=0,3
    while att<max_att:
        u,p=input("\nUser:"),input("PIN:")
        if u in accounts and accounts[u]['pin']==p:
            print("Login Successful!")
            atm_menu(accounts[u],u)
            break
        else:
            att+=1
            print(f"Invalid! Left:{max_att-att}")
if __name__=="__main__":main()