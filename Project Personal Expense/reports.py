def highest_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense.amount > highest.amount:
            highest = expense

    print("\nHighest Expense")
    print("Amount:", highest.amount)
    print("Category:", highest.category)
    print("Description:", highest.description)

def show_categories(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    categories = []

    for expense in expenses:
        if expense.category not in categories:
            categories.append(expense.category)

    print("\nCategories")
    for category in categories:
        print(category)