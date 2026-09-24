# category_summary.py
# Groups expenses by category using a dictionary and adds up the amount spent in each category.

def category_totals(expenses):
    totals = {}
    for e in expenses:
        cat = e["category"]
        if cat in totals:
            totals[cat] = totals[cat] + e["amount"]
        else:
            totals[cat] = e["amount"]
    return totals


def print_category_totals(expenses):
    totals = category_totals(expenses)
    if len(totals) == 0:
        print("No expenses recorded yet.")
        return
    for category, amount in totals.items():
        print(f"{category:<15} : {amount}")
