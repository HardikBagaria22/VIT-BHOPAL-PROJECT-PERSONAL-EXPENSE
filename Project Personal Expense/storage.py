from expense import Expense

FILE_NAME = "expenses.txt"

def save_expenses(expenses):
    file = open(FILE_NAME, "w")

    for expense in expenses:
        file.write(expense.to_string() + "\n")

    file.close()

def load_expenses():
    expenses = []

    file = open(FILE_NAME, "a")
    file.close()

    file = open(FILE_NAME, "r")

    for line in file:
        line = line.strip()

        if line != "":
            data = line.split(",")

            if len(data) == 3:
                amount = float(data[0])
                category = data[1]
                description = data[2]

                expense = Expense(amount, category, description)
                expenses.append(expense)

    file.close()
    return expenses