
print("================================")
print("       WELCOME TO MAMI BANKING")
print("================================")

# Account details
balance = 50000
atm_cash = 100000
correct_pin = "1234"
attempts = 0
max_attempts = 3

# Insert card
print("\n1. Insert Card")
print("2. Cancel")

card = input("Select an option (1-2): ")

if card == "1":
    print("Card inserted successfully!")
    print("Card verified successfully!")

    # PIN verification
    while attempts < max_attempts:
        pin = input("Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("PIN accepted!")
            break
        else:
            attempts += 1
            print("Incorrect PIN. Try again.")

    if attempts == max_attempts and pin != correct_pin:
        print("Maximum attempts reached. Transaction blocked.")

    else:
        # Main ATM menu
        while True:
            print("\n================================")
            print("          MAMI BANKING MENU")
            print("================================")
            print("1. Check Account Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")
            print("================================")

            choice = input("Select an option (1-4): ")

            # Check balance
            if choice == "1":
                print("Your account balance is:", balance)

            # Withdraw money
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to withdraw: "))

                    if amount <= 0:
                        print("Enter a valid amount.")

                    elif amount > balance:
                        print("Insufficient funds!")

                    elif amount > atm_cash:
                        print("ATM does not have enough cash.")

                    else:
                        balance -= amount
                        atm_cash -= amount
                        print("Withdrawal successful!")
                        print("Please collect your cash.")
                        print("Remaining balance:", balance)

                except ValueError:
                    print("Please enter a valid number.")

            # Deposit money
            elif choice == "3":
                try:
                    amount = float(input("Enter amount to deposit: "))

                    if amount <= 0:
                        print("Enter a valid amount.")

                    else:
                        balance += amount
                        print("Deposit successful!")
                        print("New account balance:", balance)

                except ValueError:
                    print("Please enter a valid number.")

            # Exit ATM
            elif choice == "4":
                print("Thank you for banking with us!")
                break

            else:
                print("Invalid option. Please select 1-4.")

            # Ask whether to continue
            continue_choice = input(
                "\nWould you like to perform another transaction?\n"
                "1. Yes\n"
                "2. No\n"
                "Select an option: "
            )

            if continue_choice == "2":
                print("Thank you for banking with us!")
                break

            elif continue_choice != "1":
                print("Invalid option. Returning to main menu.")

elif card == "2":
    print("Transaction cancelled.")

else:
    print("Invalid option. Please select 1 or 2.")

print("Please take your card.")
print("TRANSACTION ENDED")
