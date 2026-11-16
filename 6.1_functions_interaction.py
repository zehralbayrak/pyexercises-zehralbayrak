"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list of monthly sales figures from exercise 4.0 (January to August, in euros)
# 2. Process, function by function: average_monthly_sales() returns the average month; is_above() says if one value is higher than another; month_name() turns a month number into its name; months_above_average() goes through my list and uses the three of them to keep the names of the months above the average
# 3. Out: a list with the names of the months that sold more than the average month
# 4. The question my fourth function answers: which months sold more than the average month? Splitting it into three makes it easier to check, because I can test each small function on its own with an input where I already know the answer. If the final result is wrong, the three tests show me which part is broken.


# Your code below

# My sales list from exercise 4.0 (January to August, in euros)
monthly_sales = [12500, 9800, 14200, 11000, 15600, 13400, 10200, 16800]

# The month names in calendar order, so position 1 is January
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]


# Small function 1: returns the average sales per month (the same function as in 6.0)
def average_monthly_sales(sales):
    if len(sales) == 0:
        return None
    return sum(sales) / len(sales)


# Small function 2: returns True if the value is higher than the threshold
# A month exactly equal to the average does not count as above it
def is_above(value, threshold):
    return value > threshold


# Small function 3: turns a month number into its name (1 gives January)
# The list starts at position 0, so I take position - 1
def month_name(position):
    return month_names[position - 1]


# Fourth function: uses the three small ones to find the months above the average month
def months_above_average(sales):
    average = average_monthly_sales(sales)
    result = []
    for position, value in enumerate(sales, start=1):
        if is_above(value, average):
            result.append(month_name(position))
    return result


# Testing each small function on its own before combining them
# Test 1: average_monthly_sales([10, 20, 30]) should give 20.0
print("Test 1:", average_monthly_sales([10, 20, 30]))
# Test 2: is_above(15000, 12000) should give True
print("Test 2:", is_above(15000, 12000))
# Test 3: month_name(3) should give March
print("Test 3:", month_name(3))

# The answer to my question, using all the functions together
print(f"Average month: {average_monthly_sales(monthly_sales):.2f} euros")
print("Months above the average month:", months_above_average(monthly_sales))

