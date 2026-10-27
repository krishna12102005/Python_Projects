def showBalance():
    print(f"Your balance is ${balance:.2f} ")

def deposited(balance):
    amount  = float(input("Enter the amount to deposite: "))
    return balance + amount

def withdrawn(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if(amount > balance):
        print("your are not have a insuffienct balance")

    if(amount < 0):
        print("Enter a valid amount to withdraw")
    return balance - amount



balance = 0
is_running = True


while is_running:
    print("***** Bank Program *****")
    print("Please make the choice below (1-4)")
    print("1.Show Balance")
    print("2.Deposite Money")
    print("3.Withdraw Money")
    print("4.Exit")


    choice  = input("Enter the above choices: ")

    if choice == "1":
        showBalance()
    elif choice == "2":
        print("Your deposited amount" ,deposited(balance))
    elif choice == "3":
        print("Your withdrawn amount" , withdrawn(balance))
    else:
        is_running = False
        print("Thank you for coming to the bank")

