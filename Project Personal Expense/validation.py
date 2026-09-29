def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def get_category():
    while True:
        category = input("Enter category: ")
        if category != "":
            return category
        else:
            print("Category cannot be empty.")


def get_description():
    while True:
        description = input("Enter description: ")
        if description != "":
            return description
        else:
            print("Description cannot be empty.")