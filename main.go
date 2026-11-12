
package main

import "fmt"

func main() {
    var pin, choice, account string
    var amount, balance, atmCash float64

    balance = 50000
    atmCash = 100000

    fmt.Println("WELCOME TO THE ATM")

    // Insert and verify card
    var card string
    fmt.Print("Insert your card (yes/no): ")
    fmt.Scan(&card)

    if card != "yes" {
        fmt.Println("Card error. Transaction ended.")
        return
    }

    // PIN verification
    attempts := 0
    for attempts < 3 {
        fmt.Print("Enter your 4-digit PIN: ")
        fmt.Scan(&pin)

        if pin == "1234" {
            break
        }

        attempts++
        fmt.Println("Incorrect PIN. Try again.")
    }

    if pin != "1234" {
        fmt.Println("Maximum attempts reached. Card blocked.")
        return
    }

    // Select transaction
    fmt.Println("1. Withdraw Cash")
    fmt.Print("Select an option: ")
    fmt.Scan(&choice)

    if choice != "1" {
        fmt.Println("Invalid option. Transaction ended.")
        return
    }

    // Select account type
    fmt.Println("1. Savings")
    fmt.Println("2. Current")
    fmt.Print("Select account type: ")
    fmt.Scan(&account)

    if account != "1" && account != "2" {
        fmt.Println("Invalid account type.")
        return
    }

    // Withdraw money
    fmt.Print("Enter withdrawal amount: ")
    fmt.Scan(&amount)

    if amount <= 0 {
        fmt.Println("Invalid amount.")
        return
    }

    if amount > balance {
        fmt.Println("Insufficient funds.")
        return
    }

    if amount > atmCash {
        fmt.Println("ATM does not have enough cash.")
        return
    }

    // Authorise and dispense cash
    fmt.Println("Withdrawal authorised.")
    fmt.Println("Please collect your cash.")

    // Update account
    balance -= amount
    atmCash -= amount

    fmt.Println("Transaction successful!")
    fmt.Printf("Remaining balance: %.2f\n", balance)

    // Receipt option
    var receipt string
    fmt.Print("Do you want a receipt? (yes/no): ")
    fmt.Scan(&receipt)

    if receipt == "yes" {
        fmt.Println("Printing receipt...")
        fmt.Println("Receipt printed successfully.")
    }

    fmt.Println("Please collect your card.")
    fmt.Println("Thank you for using our ATM!")
}
