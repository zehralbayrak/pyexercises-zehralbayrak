"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the number of conversions a campaign got, typed by the user. The cost of the campaign (1200 EUR)
#    is fixed in the code.
# 2. Process: the program divides the cost by the number of conversions to get the cost per conversion.
#    Before that it checks the answer: an empty line, a word or a negative number gets a clear message and
#    another try, with 3 attempts in total. Zero gets its own message and ends the program.
# 3. Out: the cost per conversion with two decimals (30.00 EUR for 40 conversions), or a message that says
#    why there is no result.
# 4. The two failures, and whether they deserve the same message:
#    - Something that is not a whole number ("abc", "2.5"): int() raises ValueError. This is a typo, so the
#      message says what to type and the user gets another try.
#    - Zero: the division raises ZeroDivisionError. This is not a typo, it is real information (the money was
#      spent without a single conversion), so it gets a different message and the program does not ask again.
#    So no, they should not get the same message: different causes need different explanations.
#    I allow 3 attempts: enough to fix a typo, without asking forever.


# Your code below

# The cost of the campaign this month, in euros, and how many wrong answers I accept before stopping
CAMPAIGN_COST = 1200
MAX_ATTEMPTS = 3


# Asks for the number of conversions and returns the cost per conversion, or None if there is no result.
# I catch each error separately because they need different messages and different actions.
# A single "except Exception" would treat a typo and zero conversions the same way, and it would also hide
# real mistakes in my own code (a misspelled variable name, for example) behind a message that is wrong.
def ask_cost_per_conversion():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        answer = input("How many conversions did the campaign get? ").strip()
        attempts = attempts + 1

        # Empty line: the user pressed Enter without typing anything, so I say exactly that
        if answer == "":
            print("You did not type anything. Please type a whole number, like 40.")
            continue

        try:
            conversions = int(answer)
            # A negative number is a whole number, but it makes no sense for conversions
            if conversions < 0:
                print("Conversions cannot be negative. Please type 0 or more.")
                continue
            return CAMPAIGN_COST / conversions

        # Not a whole number: probably a typo, so the user gets another try
        except ValueError:
            print(f'"{answer}" is not a whole number. Please type digits only, like 40.')

        # Zero conversions: a real answer, so the program explains what it means and does not ask again
        except ZeroDivisionError:
            print(f"0 conversions: the {CAMPAIGN_COST} EUR were spent without a single conversion,")
            print("so there is no cost per conversion to calculate. This campaign needs to be checked.")
            return None

    # Too many wrong answers: stop politely instead of asking forever
    print(f"{MAX_ATTEMPTS} attempts without a valid number. Stopping here, nothing was calculated.")
    return None


# Main part: one calculation. Ctrl+C or Ctrl+D also end the program with a message instead of an error.
print(f"Cost per conversion for a campaign that cost {CAMPAIGN_COST} EUR")
try:
    cost = ask_cost_per_conversion()
    if cost is not None:
        print(f"Cost per conversion: {cost:.2f} EUR")
except (KeyboardInterrupt, EOFError):
    print()
    print("Stopped by the user. Nothing was calculated.")

# Check it yourself (what happened when I ran it):
# Run 1, "40": it printed "Cost per conversion: 30.00 EUR" (1200 / 40 = 30).
# Run 2, "0": it explained that the 1200 EUR were spent without a conversion and ended normally, without asking again.
# Run 3, "abc": it said "abc" is not a whole number and asked again. I typed 40 and got 30.00 EUR.
# Run 4, an empty line: it said I did not type anything and asked again. After 3 empty lines it stopped with a message.
# None of the four runs stopped the program with a Python error.