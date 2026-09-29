from expense import Expense
from storage import save_expenses

def add_expense(expenses, amount, category, description):
    new_expense = Expense(amount, category, description)
    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added.")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return
    print("\nAll Expenses")
    number = 1
    for expense in expenses:
        expense.display(number)
        number = number + 1

def calculate_total(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return
    total = 0
    for expense in expenses:
        total = total + expense.amount
    print("Total Expense:", total)

def category_total(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return
    category = input("Enter category: ")
    total = 0
    for expense in expenses:
        if expense.category == category:
            total = total + expense.amount
    print("Category Total:", total)

def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return
    view_expenses(expenses)
    number = int(input("Enter expense number: "))
    if number >= 1 and number <= len(expenses):
        del expenses[number - 1]
        save_expenses(expenses)
        print("Expense deleted.")
    else:
        print("Invalid number.")