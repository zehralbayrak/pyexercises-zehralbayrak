"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the list of 8 monthly sales figures from exercise 4.0
# 2. Process: the program puts the figures in four different orders, working on copies so the original stays the same
# 3. Out: the list in four orders, then the original list on the last line to prove it has not changed
# 4. My four orders, and which ones modify the original: lowest to highest, highest to lowest, last month first, random order; sort(), reverse() and shuffle() change a list in place, so I used shuffle() only on a copy and my original is never modified


# Your code below

import random

# The same monthly sales list as in exercise 4.0 (January to August, in euros)
monthly_sales = [12500, 9800, 14200, 11000, 15600, 13400, 10200, 16800]

# Order 1: sorted() returns a new list, the original is not touched
print("Lowest to highest:", sorted(monthly_sales))

# Order 2: sorted() with reverse=True, also a new list
print("Highest to lowest:", sorted(monthly_sales, reverse=True))

# Order 3: [::-1] makes a reversed copy, so the last month comes first
print("Last month first:", monthly_sales[::-1])

# Order 4: shuffle() changes a list in place, so I shuffle a copy instead of the original
shuffled_sales = monthly_sales.copy()
random.shuffle(shuffled_sales)
print("Random order:", shuffled_sales)

# Proof: the original list must still be in month order
print("Original list:", monthly_sales)


# test (what happened when I ran it):
# the last line showed [12500, 9800, 14200, 11000, 15600, 13400, 10200, 16800]
# I compared it item by item with my list from 4.0: all 8 items are the same and in the same order
# the random order is different every time I run the program, because shuffle() mixes the copy again each time