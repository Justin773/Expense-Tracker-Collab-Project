import os
from datetime 
import datetime

# File to store expenses
EXPENSES_FILE = "expenses.txt"

# List to store expenses
expenses = []

def load_expenses():
    #Load expenses from a file if it exists
    global expenses
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                category, amount, date = line.strip().split("|")
                expenses.append({
                    "category": category,
                    "amount": float(amount),
                    "date": date
                })
        print("Expenses loaded successfully!")
    else:
        print("No existing expense file found. Starting with an empty list.")

def save_expenses():
    #Save expenses to a file
    with open(EXPENSES_FILE, "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']}|{expense['amount']}|{expense['date']}\n")
    print("Expenses saved successfully!")

def add_expense():
    #Adds a new expense to the expenses list
    category = input("Enter expense category (e.g., Food, Transport, Entertainment): ").strip()
    
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid positive amount (e.g., 10.50).")
    
    while True:
        date = input("Enter expense date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    expenses.append({"category": category, "amount": amount, "date": date})
    print("Expense added successfully!")

def view_expenses():
    #Displays all expenses
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Date: {expense['date']}")
    print("--------------------\n")

def calculate_total_expenses():
    #Calculates and displays the total amount of all expenses
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")

def filter_expenses_by_category():
    #Filters and displays expenses by a specific category
    category = input("Enter category to filter by: ").strip()
    filtered_expenses = [expense for expense in expenses if expense['category'].lower() == category.lower()]
    
    if not filtered_expenses:
        print(f"No expenses found for category: {category}")
    else:
        print(f"\n--- Expenses for {category} ---")
        for i, expense in enumerate(filtered_expenses, start=1):
            print(f"{i}. Amount: ${expense['amount']:.2f}, Date: {expense['date']}")
        print("------------------------\n")

def delete_expense():
    """Deletes a specific expense by selecting from a list."""
    if not expenses:
        print("No expenses to delete.")
        return
    
    view_expenses()
    
    while True:
        try:
            choice = int(input("Enter the number of the expense to delete: "))
            if 1 <= choice <= len(expenses):
                deleted_expense = expenses.pop(choice - 1)
                print(f"Expense deleted: Category: {deleted_expense['category']}, Amount: ${deleted_expense['amount']:.2f}, Date: {deleted_expense['date']}")
                return
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_summary():
    #Generates a summary of expenses by category
    if not expenses:
        print("No expenses found.")
        return
    
    summary = {}
    for expense in expenses:
        category = expense['category']
        if category in summary:
            summary[category] += expense['amount']
        else:
            summary[category] = expense['amount']
    
    print("\n--- Expense Summary by Category ---")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
    print("----------------------------------\n")

def main():
    #Main function to run the expense tracker program
    load_expenses()
    
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Delete Expense")
        print("6. Generate Expense Summary")
        print("7. Save and Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses_by_category()
        elif choice == "4":
            calculate_total_expenses()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            generate_summary()
        elif choice == "7":
            save_expenses()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    main()