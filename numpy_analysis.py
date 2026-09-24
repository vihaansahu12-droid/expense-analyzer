# numpy_analysis.py
# Uses NumPy arrays to analyze the expense amounts.
# Functions used here (array, sum, max, min, where, nonzero) 

from numpy import array, sum as np_sum, max as np_max, min as np_min, where, nonzero


def get_amounts_array(expenses):
    amounts = []
    for e in expenses:
        amounts.append(e["amount"])
    return array(amounts)


def total_spent(expenses):
    if len(expenses) == 0:
        return 0
    amounts = get_amounts_array(expenses)
    return np_sum(amounts)


def average_spent(expenses):
    if len(expenses) == 0:
        return 0
    total = total_spent(expenses)
    return total / len(expenses)


def highest_expense(expenses):
    if len(expenses) == 0:
        return 0
    amounts = get_amounts_array(expenses)
    return np_max(amounts)


def lowest_expense(expenses):
    if len(expenses) == 0:
        return 0
    amounts = get_amounts_array(expenses)
    return np_min(amounts)


def flag_over_budget(expenses, budget):
    # uses where() to keep amounts above budget, replace the rest with 0
    if len(expenses) == 0:
        return []
    amounts = get_amounts_array(expenses)
    flagged = where(amounts > budget, amounts, 0)
    return flagged


def over_budget_expenses(expenses, budget):
    # uses nonzero() to find the positions where spending crossed the budget
    if len(expenses) == 0:
        return []
    amounts = get_amounts_array(expenses)
    positions = nonzero(amounts > budget)
    result = []
    for i in positions[0]:
        result.append(expenses[i])
    return result
