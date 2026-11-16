"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answer to "Has the client paid invoice 1043?", typed up to 3 times
# 2. Process: the program cleans each answer with strip() and lower(), counts the attempts, and stops when the answer is "yes" or after 3 attempts
# 3. Out: a summary with the number of attempts, the answers given, and whether the invoice is paid
# 4. My stop condition, my attempt limit, my summary: the loop stops when the answer is "yes" ("Yes" and " yes " count too, because the user means the same thing); the limit is 3 attempts, then the program stops and says the client must be called; the summary shows the attempts, the answers and whether the invoice is paid

# Your code below

# My limits: at most 3 attempts; the loop stops early if the answer is "yes"
max_attempts = 3
attempts = 0
paid = False
answers = []

# Keeps asking until the client has paid or the limit is reached
while attempts < max_attempts:
    # strip() removes extra spaces and lower() removes capitals, so "Yes", "yes" and " yes " count the same
    answer = input("Has the client paid invoice 1043? (yes/no): ").strip().lower()
    attempts = attempts + 1
    answers.append(answer)
    if answer == "yes":
        paid = True
        break

# Summary of what happened during the loop
print("Attempts:", attempts)
print("Answers given:", answers)
if paid:
    print("The invoice is paid.")
else:
    print("Limit reached: the invoice is still unpaid, the client must be called.")


# test (what happened when I ran it):
# never the expected answer (no, no, no): the program stopped after 3 attempts and said the client must be called, so it does not run for ever
# capitals and extra spaces (" YES"): the answer was saved as 'yes' and the program stopped after 1 attempt, so strip() and lower() work
# no, no, yes: the program stopped at the third attempt because the answer was "yes", and the summary said the invoice is paid