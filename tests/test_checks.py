# test_checks.py
# Simple checks for the core functions, using plain if/else and print

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import expense_input
import numpy_analysis
import category_summary
import sort_search

pass_count = 0
fail_count = 0


def check(description, actual, expected):
    global pass_count, fail_count
    if actual == expected:
        print("PASS:", description)
        pass_count = pass_count + 1
    else:
        print("FAIL:", description, "-> expected", expected, "but got", actual)
        fail_count = fail_count + 1


def test_add_valid_expense():
    expenses = []
    success, message = expense_input.add_expense(expenses, "2026-09-01", "Food", "100", "Lunch")
    check("add_expense returns True for valid amount", success, True)
    check("expense list has 1 item after adding", len(expenses), 1)


def test_add_invalid_amount():
    expenses = []
    success, message = expense_input.add_expense(expenses, "2026-09-01", "Food", "-50", "Lunch")
    check("add_expense returns False for negative amount", success, False)
    check("expense list stays empty when amount is invalid", len(expenses), 0)


def test_total_and_average():
    expenses = []
    expense_input.add_expense(expenses, "2026-09-01", "Food", "100", "Lunch")
    expense_input.add_expense(expenses, "2026-09-02", "Transport", "50", "Bus")
    check("total_spent adds amounts correctly", numpy_analysis.total_spent(expenses), 150.0)
    check("average_spent calculates correctly", numpy_analysis.average_spent(expenses), 75.0)


def test_category_totals():
    expenses = []
    expense_input.add_expense(expenses, "2026-09-01", "Food", "100", "Lunch")
    expense_input.add_expense(expenses, "2026-09-02", "Food", "50", "Snacks")
    totals = category_summary.category_totals(expenses)
    check("category_totals adds Food expenses together", totals["Food"], 150.0)


def test_bubble_sort():
    expenses = []
    expense_input.add_expense(expenses, "2026-09-01", "Food", "300", "A")
    expense_input.add_expense(expenses, "2026-09-02", "Transport", "100", "B")
    expense_input.add_expense(expenses, "2026-09-03", "Rent", "500", "C")
    sorted_list = sort_search.bubble_sort_by_amount(expenses)
    check("bubble sort orders amounts lowest to highest",
          [e["amount"] for e in sorted_list], [100.0, 300.0, 500.0])


def test_sequential_search():
    expenses = []
    expense_input.add_expense(expenses, "2026-09-01", "Food", "100", "A")
    expense_input.add_expense(expenses, "2026-09-02", "Transport", "50", "B")
    results = sort_search.sequential_search_by_category(expenses, "Food")
    check("sequential search finds the correct category", len(results), 1)


test_add_valid_expense()
test_add_invalid_amount()
test_total_and_average()
test_category_totals()
test_bubble_sort()
test_sequential_search()

print()
print("Passed:", pass_count, "  Failed:", fail_count)
