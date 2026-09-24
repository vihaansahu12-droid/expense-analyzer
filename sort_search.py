# sort_search.py
# Bubble sort to sort expenses by amount, and sequence search to find expenses in a given category.

def bubble_sort_by_amount(expenses):
    data = expenses.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]["amount"] > data[j + 1]["amount"]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    return data


def sequential_search_by_category(expenses, category):
    results = []
    for e in expenses:
        if e["category"].lower() == category.lower():
            results.append(e)
    return results
