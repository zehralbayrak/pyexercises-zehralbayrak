"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of 8 monthly sales figures in euros, written in the code
# 2. Process: the program shows the list, picks one month, sorts the figures from lowest to highest and adds them up
# 3. Out: four lines: the whole list, the sales of one month, the sorted list and the total
# 4. What my list is about, and what I computed from it: the monthly sales of one store from January to August; I computed the total, which shows how much the store sold over the period and can be compared with its target or with last year


# Your code below

# Sales of one store for each month from January to August, in euros
monthly_sales = [12500, 9800, 14200, 11000, 15600, 13400, 10200, 16800]

# Shows the whole list
print("Monthly sales:", monthly_sales)

# Shows one item: index 4 is May, because counting starts at 0
print("Sales in May:", monthly_sales[4])

# sorted() gives a sorted copy and keeps the original order of the months
print("Sales from lowest to highest:", sorted(monthly_sales))

# sum() adds all the items to get the total sales of the period
total_sales = sum(monthly_sales)
print("Total sales from January to August:", total_sales)


# test (what happened when I ran it):
# by hand, the first three months: 12500 + 9800 + 14200 = 36500
# sum(monthly_sales[:3]) also gave 36500, so the program agrees with my calculation
# total for all eight months: 103500