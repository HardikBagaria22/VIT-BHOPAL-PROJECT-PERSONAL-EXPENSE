class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def display(self, number):
        print(
            number,
            "| Amount:", self.amount,
            "| Category:", self.category,
            "| Description:", self.description
        )

    def to_string(self):
        return str(self.amount) + "," + self.category + "," + self.description