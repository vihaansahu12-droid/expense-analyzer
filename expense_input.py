# expense_input.py
# Add new expenses and view the list of expenses Each expense is stored as a dictionary inside a list.

from validators import is_valid_amount, is_non_empty

SUGGESTED_CATEGORIES = ["Food", "Transport", "Rent", "Utilities",
                         "Entertainment", "Health", "Shopping", "Other"]


def add_expense(expenses, date, category, amount_text, note):
    if is_non_empty(date) == False:
        return False, "Date cannot be empty."
    if is_non_empty(category) == False:
        return False, "Category cannot be empty."
    if is_valid_amount(amount_text) == False:
        return False, "Amount must be a positive number."

    # normalizing so "food", "FOOD", "Food" are all treated as the same category
    clean_category = category.strip().title()

    new_expense = {
        "date": date,
        "category": clean_category,
        "amount": float(amount_text),
        "note": note
    }
    expenses.append(new_expense)
    return True, "Expense added."


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    print(f"{'Date':<12}{'Category':<15}{'Amount':<10}Note")
    print("-" * 50)
    for e in expenses:
        print(f"{e['date']:<12}{e['category']:<15}{e['amount']:<10}{e['note']}")
