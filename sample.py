balance = 1000
pin_code = 1111

pin_attempts = 3
while pin_attempts > 0:
    x = int(input("enter your security pin: "))
    if x == pin_code:
        print("Access granted!")
        break
    else:
        pin_attempts -= 1
        print(f"Incorrect pin. You have {pin_attempts} attempts remaining.")
else:
    print("card blocked due to too many incorrect attempts")
    exit()

def atm_simulation():
    global balance
    print("Welcome to the ATM simulation")
    print("1. Check amount")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        print(balance)
        
    elif choice == 2:
        deposit_val = int(input("enter value you would like to deposit:"))
        balance += deposit_val
        print(f"successfully deposited {deposit_val} to balance. Current balance: {balance}")

    elif choice == 3:
        withdraw_val = int(input("enter value you would like to withdraw: "))
        balance -= withdraw_val
        print(f"successfully withdrew {withdraw_val} from balance. Current balance: {balance}")

    elif choice == 4:
        print("Thank you for using our ATM simulation")
    else:
        print("invalid choice!")

atm_simulation()
input("press the enter key to exit")