from storage import load_expenses
from expense_manager import add_expense, view_expenses, calculate_total, category_total, delete_expense
from reports import highest_expense, show_categories
from validation import get_amount, get_category, get_description

def show_menu():
    print("\nPERSONAL EXPENSE TRACKER")
    print("""
         1. Add Expense
         2. View Expenses
         3. Calculate Total
         4. Category-wise Total
         5. Delete Expense
         6. Highest Expense
         7. Show Categories
         8. Exit""")

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = get_amount()
            category = get_category()
            description = get_description()
            add_expense(expenses, amount, category, description)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            calculate_total(expenses)

        elif choice == "4":
            category_total(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            highest_expense(expenses)

        elif choice == "7":
            show_categories(expenses)

        elif choice == "8":
            print("Thank you for using Personal Expense Tracker.")
            break

        else:
            print("Invalid choice.")

main()