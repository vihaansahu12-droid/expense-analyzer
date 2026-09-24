# main.py
# Personal Expense Analyzer - command line program. Data is entered analyzed and organised in this code.
# you can run the code by typing "python main.py" in the terminal

import expense_input
import numpy_analysis
import category_summary
import sort_search


def show_menu():
    print("\n----- EXPENSE ANALYZER -----")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Category-wise summary")
    print("4. Show total, average, highest, lowest")
    print("5. Show expenses over a budget limit")
    print("6. View expenses sorted by amount")
    print("7. Search expenses by category")
    print("0. Exit")


def main():
    expenses = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Date: ")
            print("Suggested categories:", ", ".join(expense_input.SUGGESTED_CATEGORIES))
            category = input("Category: ")
            amount_text = input("Amount: ")
            note = input("Note: ")
            success, message = expense_input.add_expense(expenses, date, category, amount_text, note)
            print(message)

        elif choice == "2":
            expense_input.view_expenses(expenses)

        elif choice == "3":
            category_summary.print_category_totals(expenses)

        elif choice == "4":
            if len(expenses) == 0:
                print("No expenses recorded yet.")
            else:
                print("Total spent   :", numpy_analysis.total_spent(expenses))
                print("Average spent :", numpy_analysis.average_spent(expenses))
                print("Highest expense:", numpy_analysis.highest_expense(expenses))
                print("Lowest expense :", numpy_analysis.lowest_expense(expenses))

        elif choice == "5":
            budget_text = input("Enter budget limit: ")
            budget = float(budget_text)
            over_list = numpy_analysis.over_budget_expenses(expenses, budget)
            if len(over_list) == 0:
                print("No expenses went over the budget limit.")
            else:
                print("Expenses over budget:")
                expense_input.view_expenses(over_list)

        elif choice == "6":
            sorted_expenses = sort_search.bubble_sort_by_amount(expenses)
            expense_input.view_expenses(sorted_expenses)

        elif choice == "7":
            category = input("Enter category to search: ")
            results = sort_search.sequential_search_by_category(expenses, category)
            expense_input.view_expenses(results)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
