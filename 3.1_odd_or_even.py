"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one number N typed by the user; input() gives text, so int() turns it into a whole number
# 2. Process: the program goes through every number from 1 to N and checks whether it can be divided by 2 with nothing left over
# 3. Out: one line for each number, saying whether it is odd or even
# 4. What happens on 0, on a negative number, on a very large number: on 0 or a negative number the program shows a message and stops, because there is nothing to count from 1; above 100 it shows a message and stops, so the screen does not fill with hundreds of lines


# Your code below

# asks for a number N; int() turns the typed text into a whole number
n = int(input("Enter a number: "))

# my decisions: below 1 or above 100, show a message and stop; otherwise check every number from 1 to N
if n < 1:
    print("Please enter a number greater than 0.")
elif n > 100:
    print("Please enter a number of 100 or less.")
else:
    # range(1, n + 1) gives every number from 1 to N; % 2 gives what is left over after dividing by 2
    for number in range(1, n + 1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")


# test (what happened when I ran it):
# 6: 1, 3, 5 are odd and 2, 4, 6 are even, so three odd and three even, as expected
# 0: the program showed "Please enter a number greater than 0." and stopped, as I decided
# -4: the program showed the same message and stopped, as I decided
# 5000: the program showed "Please enter a number of 100 or less." and stopped, as I decided
