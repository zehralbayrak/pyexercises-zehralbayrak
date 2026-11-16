"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the list of 8 monthly sales figures from exercise 4.0, and a monthly target of 12000 euros that I chose
# 2. Process: for each month, the program takes its position and its sales and checks whether the sales reach the target
# 3. Out: 8 lines, one per month, with the month number, the sales and whether the target was reached
# 4. What I compute for each item, and why it is worth showing: whether each month reached the 12000 euro target; the reader sees at a glance which months went well and which need attention


# Your code below

# The monthly sales list from exercise 4.0 (January to August, in euros)
monthly_sales = [12500, 9800, 14200, 11000, 15600, 13400, 10200, 16800]

# My decision: the store's monthly target is 12000 euros
target = 12000

# For every month: its position (1 = January), its sales, and whether it reached the target
for position, sales in enumerate(monthly_sales, start=1):
    if sales >= target:
        result = "target reached"
    else:
        result = "below target"
    print("Month", position, ":", sales, "euros,", result)


# test (what happened when I ran it):
# the program printed 8 lines and my list has 8 items, so there is no off-by-one
# months 1, 3, 5, 6 and 8 reached the 12000 euro target; months 2, 4 and 7 were below it
# start=1 makes the first month "Month 1"; without it, January would be "Month 0"