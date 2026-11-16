"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of monthly sales figures in euros, like my January to August list from exercise 4.0
# 2. Process: the function first checks if the list is empty; if not, it adds up all the figures with sum() and divides the total by the number of months with len()
# 3. Out: the average sales per month, as a number that the function returns (it does not print it), or None if the list is empty
# 4. My function name, and why return rather than print: average_monthly_sales. Yes, the name says what it does without reading the code: it gives back the average of the monthly sales. I return the result instead of printing it because a printed value only appears on the screen and is then gone (the function gives back None). A returned value can be stored in a variable, rounded, compared or passed to another function, like I do at the end when I compare two periods.


# Your code below

# My sales list from exercise 4.0 (January to August, in euros)
monthly_sales = [12500, 9800, 14200, 11000, 15600, 13400, 10200, 16800]


# Returns the average sales per month for any list of monthly figures
# An empty list has no months, so there is no average: the function returns None instead of crashing
def average_monthly_sales(sales):
    if len(sales) == 0:
        return None
    return sum(sales) / len(sales)


# Three calls with three different inputs: the whole period, the first quarter, the summer months
whole_period = average_monthly_sales(monthly_sales)
first_quarter = average_monthly_sales(monthly_sales[:3])
summer = average_monthly_sales(monthly_sales[5:])

# Display the three results with two decimals
print(f"January to August: {whole_period:.2f} euros per month")
print(f"January to March: {first_quarter:.2f} euros per month")
print(f"June to August: {summer:.2f} euros per month")

# Because the function returns its result, I can reuse it here to compare two periods
if summer > first_quarter:
    print("Summer months sold more on average than the first quarter")
else:
    print("The first quarter sold more on average than the summer months")

# Check it yourself: the function with an empty list
print("Empty list:", average_monthly_sales([]))

# Check it yourself (what happened when I ran it):
# Before the fix, average_monthly_sales([]) crashed with ZeroDivisionError: division by zero,
# because an empty list has 0 months and Python cannot divide by 0
# I decided the crash is not acceptable: one empty list would stop the whole program
# Returning 0 would also be wrong, because it looks like a period with no sales at all
# So the function now returns None, which means "no average", and the program prints Empty list: None