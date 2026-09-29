# Personal Expense Tracker

## Overview
Personal Expense Tracker is a simple Python project that helps users keep track of their daily expenses. It allows users to add, view, calculate and delete expenses using a command-line interface.

## Features
- Add expenses
- View expenses
- Calculate total expenses
- Calculate category-wise total
- Delete expenses
- Find highest expense
- Show categories
- Save and load expenses
- Check user input

## Technologies Used
- Python
- VS Code
- Text file for storing expenses

## Project Structure
- `main.py` - Runs the main program and shows the menu
- `expense.py` - Contains the Expense class
- `expense_manager.py` - Handles adding, viewing and deleting expenses
- `storage.py` - Saves and loads expenses
- `validation.py` - Checks user input
- `reports.py` - Handles expense reports
- `expenses.txt` - Stores expense data
- `statement.md` - Contains project statement

## How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```text
python main.py

4. Select an option from the menu.

## Testing
The project was tested by adding, viewing, calculating and deleting expenses. Invalid inputs such as text instead of a number, negative amounts and empty fields were also tested.

## Future Improvements
- Add a monthly expense report
- Add a simple graphical interface
- Add more ways to analyze expenses