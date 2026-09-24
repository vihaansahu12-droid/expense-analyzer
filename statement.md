# Problem Statement

## Problem

A lot of the time people don't really keep track of where their money
is going. There's no quick way to add everything up or see which
category is eating most of the budget until it's too late. This
project is basically a simple command-line tool where you punch in
your expenses and it does the adding up and analysis for you.

## Scope

This is meant for a single person to use from the command line. All
the data you enter only lasts for that one run of the program - it
doesn't get saved anywhere, since we haven't covered file handling in
class yet. So if you close the program, you'll need to re-enter
everything next time.

## Target Users

Basically anyone who wants a quick way to total up and look through
some expenses in one sitting - students, mainly, since that's who this
was built for. No database or saved files involved, just run it and
use it.

## Features

1. Add Expense - enter the date, category, amount, and a short note
2. View Expenses - see everything you've entered so far
3. Category-wise Summary - adds up spending per category using a dictionary
4. Statistics - total, average, highest and lowest expense, calculated with NumPy arrays
5. Budget Check - flags expenses that went over a budget limit you set, using NumPy's where() and nonzero()
6. Sort - sorts all expenses by amount using bubble sort
7. Search - lets you search expenses by category using sequential search