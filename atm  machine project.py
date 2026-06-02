balance = 1000

print("ATM machine")
print("1.balance check")
print("2.Deposite")
print("3.withrawal")
print("4.Exit")


choice = int(input("apni choice daalo: "))
if choice == 1:
    print("apka balance hai: ",balance)
    
elif choice == 2:
    
    amount = float(input("Deposite amount daalo:"))
    balance = balance + amount
    print("naya balance:",balance)
    
elif choice == 3:
    
    amount = float(input("withdrawal amount daalo:"))
    if amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        print("naya balance:",balance)
elif choice == 4:
    print("Thanks for using our ATM machine")
else:    print("Invalid choice")