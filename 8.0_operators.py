"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two values I chose myself, the word "Paris" and the same word written "paris"
# 2. Process: the program compares them with every comparison operator (==, !=, <, >, <=, >=),
#    combines some of those results with and, or and not, and compares each result with the guess
#    I wrote before running
# 3. Out: a table with one line per operation: the result, my guess, and whether my guess was right,
#    then how many I got right and why capitals change the result
# 4. My two values and the result that surprised me: "Paris" and "paris". I thought the capital P
#    would make "Paris" the bigger one, but "Paris" < "paris" is True. Python compares the letter codes:
#    "P" is 80 and "p" is 112, so words with a capital come before the same word in lower case.


# Your code below

# My two values: the same city, once with a capital letter and once without
value_a = "Paris"
value_b = "paris"

# My guesses, written before running the program (True or False for each line of the table)
predictions = {
    "a == b": False,
    "a != b": True,
    "a < b": False,
    "a > b": True,
    "a <= b": False,
    "a >= b": True,
    "(a < b) and (a != b)": False,
    "(a == b) or (a > b)": True,
    "not (a == b)": True,
    "(a <= b) and (a >= b)": False,
    "a.lower() == b.lower()": True,
}

# Every comparison between the two values
results = {
    "a == b": value_a == value_b,
    "a != b": value_a != value_b,
    "a < b": value_a < value_b,
    "a > b": value_a > value_b,
    "a <= b": value_a <= value_b,
    "a >= b": value_a >= value_b,
}

# Logical combinations of those results with and, or and not
results["(a < b) and (a != b)"] = results["a < b"] and results["a != b"]
results["(a == b) or (a > b)"] = results["a == b"] or results["a > b"]
results["not (a == b)"] = not results["a == b"]
results["(a <= b) and (a >= b)"] = results["a <= b"] and results["a >= b"]

# The same comparison without capitals, to show how to compare two words fairly
results["a.lower() == b.lower()"] = value_a.lower() == value_b.lower()

# The table: one line per operation with the result, my guess and whether I was right
print(f"Comparing {value_a!r} and {value_b!r}")
print(f"{'Operation':<26}{'Result':<8}{'My guess':<10}Right?")
print("-" * 50)
correct = 0
for operation, result in results.items():
    guess = predictions[operation]
    if guess == result:
        correct += 1
        mark = "yes"
    else:
        mark = "no"
    print(f"{operation:<26}{str(result):<8}{str(guess):<10}{mark}")
print("-" * 50)

# My score, and the reason capitals matter: Python compares the code of each letter
print(f"I predicted {correct} out of {len(results)} correctly")
print(f"Why: {value_a[0]!r} has code {ord(value_a[0])} and {value_b[0]!r} has code {ord(value_b[0])}, so capitals come first")

# Check it yourself (what happened when I ran it):
# I predicted 5 out of 11 correctly. I was wrong on every line that uses < or > because I thought a capital
# letter makes a word bigger. It is the opposite: "Paris" < "paris" is True.
# The last line shows the fix: with lower() on both sides, the two words are equal.