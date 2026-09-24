# Expense Analyzer

This is my project for the Introduction to Problem Solving and Programming
course. It's a simple command line program that lets you enter your
expenses and then analyze them a bit -
see totals, sort them, search through them, that kind of thing.

I built it using lists, dictionaries and NumPy arrays since those are
the things we've covered in the modules so far

## What it does

Basically you run the program, add some expenses (date, category, amount,
a note), and then you can:

- see all the expenses you entered
- get a category-wise total (like how much you spent on Food vs Transport)
- see your total spending, average, highest and lowest expense
- check which expenses crossed a budget limit you set
- sort everything by amount (using bubble sort)
- search for expenses in a particular category

the data doesn't get saved anywhere, so once you close the program it's gone. We haven't learned yet how to make liraries or store data in data bases Everything happens within one run.

## Files in this project

- `main.py` - the menu, this is what you actually run
- `expense_input.py` - adding and viewing expenses
- `validators.py` - checks the amount/date etc are entered properly
- `numpy_analysis.py` - all the NumPy stuff (totals, averages, budget check)
- `category_summary.py` - groups expenses by category using a dictionary
- `sort_search.py` - the bubble sort and the search function
- `tests/test_checks.py` - some basic tests I wrote to check things work

## How to run it

You need Python 3 installed. 

This project uses NumPy, so install it firs by typin "pip install numpy" in the terminal
Check for the tests by typing "python tests/test_checks.py" in the terminal
should show "Passed : 9" "Failed : 0"

Then you can run the program my typing python main.py
and follow the menu. Add a few expenses first (option 1) before trying
the analysis options, otherwise there's nothing to analyze.