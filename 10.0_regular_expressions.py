"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: three values typed by someone who signs up for the newsletter of a shop in Paris:
#    an email address, a French mobile number for SMS offers, and a postal code
# 2. Process: each value is cleaned (spaces at both ends removed) and checked against its own rule with a
#    regular expression. The program lists every field that fails and why. Only when all three pass are they
#    saved, together, as one line. Before that, it runs my nine test values to show the rules work.
# 3. Out: one new line in newsletter_signups.csv (email;phone;postal_code), or a message saying which fields
#    were rejected and that nothing was saved
# 4. My three fields, and what makes a value acceptable (in plain English, before any pattern):
#    - Email: letters, digits, dots, underscores, plus or minus signs, then exactly one @, then a domain name,
#      a dot and an ending of at least two letters (.com, .fr, .edu). No spaces anywhere.
#      Borderline: I reject "zehra@gmail" because without an ending like .com the email cannot be delivered.
#    - Mobile number: a French mobile, so 06 or 07 followed by eight more digits, or +33 instead of the first 0.
#      Spaces between the pairs of digits are allowed, dots and dashes are not.
#      Borderline: I reject landlines starting with 01 to 05, because the shop sends its offers by SMS.
#    - Postal code: exactly five digits, nothing else.
#      Borderline: in Corsica the department is "2A" or "2B", but the postal code itself still has five digits
#      (20000, 20090...), so "2A004" is rejected.


# Your code below

import csv
import os
import re

SAVE_FILE = "newsletter_signups.csv"

# Email pattern, piece by piece:
#   [A-Za-z0-9._+-]+      one or more letters, digits, dots, underscores, plus or minus signs (the name part)
#   @                     exactly one at sign (the name part cannot contain @, so a second one fails)
#   [A-Za-z0-9-]+         the domain name, like gmail or skema
#   (\.[A-Za-z0-9-]+)*    optional extra parts, like .mail in mail.skema.edu
#   \.[A-Za-z]{2,}        a dot and an ending of at least two letters, like .com or .fr
EMAIL_PATTERN = r"[A-Za-z0-9._+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"

# Mobile pattern, piece by piece:
#   (0|\+33 ?)            starts with 0, or with +33 followed by an optional space
#   [67]                  then a 6 or a 7, the two first digits of French mobile numbers
#   ( ?[0-9]{2}){4}       then four pairs of digits, each pair may have one space before it
PHONE_PATTERN = r"(0|\+33 ?)[67]( ?[0-9]{2}){4}"

# Postal code pattern: [0-9]{5} means exactly five digits
POSTAL_CODE_PATTERN = r"[0-9]{5}"

# For each field: the pattern, and the rule shown to the user when a value is rejected
RULES = {
    "email": (EMAIL_PATTERN, "name, one @, a domain and an ending like .com, no spaces"),
    "phone": (PHONE_PATTERN, "a French mobile: 06 or 07 and 8 more digits, or +33 6..., spaces allowed"),
    "postal_code": (POSTAL_CODE_PATTERN, "exactly five digits, like 75001"),
}


# Returns True if the whole value follows the rule of that field.
# fullmatch checks the entire text, so "75001abc" fails even though it starts with five digits.
def is_valid(field, value):
    pattern = RULES[field][0]
    return re.fullmatch(pattern, value) is not None


# Adds one sign-up to the file; the header line is written only the first time
def save_signup(email, phone, postal_code):
    file_is_new = not os.path.exists(SAVE_FILE) or os.path.getsize(SAVE_FILE) == 0
    with open(SAVE_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        if file_is_new:
            writer.writerow(["email", "phone", "postal_code"])
        writer.writerow([email, phone, postal_code])


# Check it yourself: for each field one value that must pass and two that must fail (nine tests)
TESTS = [
    ("email", "zehra.albayrak@skema.edu", True),
    ("email", "zehra@gmail", False),
    ("email", "zehra albayrak@gmail.com", False),
    ("phone", "06 12 34 56 78", True),
    ("phone", "01 23 45 67 89", False),
    ("phone", "06 12 34 56", False),
    ("postal_code", "75001", True),
    ("postal_code", "7500", False),
    ("postal_code", "2A004", False),
]

print("Nine test values")
print(f"{'Field':<13}{'Value':<28}{'Expected':<10}{'Got':<7}OK?")
for field, value, expected in TESTS:
    result = is_valid(field, value)
    mark = "yes" if result == expected else "SURPRISE"
    print(f"{field:<13}{value:<28}{str(expected):<10}{str(result):<7}{mark}")
print()

# The real sign-up: ask the three values, check them all, and save only if all three pass
print("Newsletter sign-up")
answers = {
    "email": input("Email: ").strip(),
    "phone": input("Mobile number: ").strip(),
    "postal_code": input("Postal code: ").strip(),
}

rejected = []
for field, value in answers.items():
    if not is_valid(field, value):
        rejected.append(field)
        print(f'Rejected {field}: "{value}" does not follow the rule ({RULES[field][1]})')

if len(rejected) == 0:
    save_signup(answers["email"], answers["phone"], answers["postal_code"])
    print("All three are valid. Saved in", SAVE_FILE)
else:
    print("Nothing was saved, because", len(rejected), "field(s) did not pass.")

# Check it yourself (what happened when I ran it):
# All nine tests gave the result I expected: three passes and six fails.
# Surprise: "zehra..albayrak@gmail.com" (two dots in a row) passes my email rule, although real email
# addresses cannot have two dots in a row. My pattern is simpler than the full email rules. For a newsletter
# I accept that, because such an email would only bounce, it would not break anything.
# Second surprise: "0612 345678" passes too, because each pair may or may not have a space before it.
# I decided that is fine: it is still a real mobile number, only written in an unusual way.