"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: what I type for one internship application: the company, the position, the date I applied
#    and where the application stands (applied, interview, offer or rejected)
# 2. Process: the program asks for each value and checks it. Company and position cannot be empty,
#    the date must be a real date (Enter means today), and the status must be one of the four words.
#    If a value is not acceptable, it explains why and asks again, so a wrong value never reaches the file.
#    Then it adds the application as one new line at the end of the file. The very first time, when the
#    file does not exist yet (or is empty), it writes the header line first, and never again after that.
# 3. Out, file name and columns: internship_applications.csv, separated by semicolons like
#    7.0_student_data.csv, with the columns company;position;date_applied;status
# 4. Why these columns, and what this file is for: I am applying for internships and need to keep track
#    of them. With two hundred rows I would count how many reached "interview" or "offer" to see my
#    success rate, find the ones still at "applied" after two weeks to send a follow-up email, and
#    compare which kinds of position answer me most often.


# Your code below

import csv
import os
from datetime import date

# The file name, the columns and the four statuses an application can have
FILE_NAME = "internship_applications.csv"
COLUMNS = ["company", "position", "date_applied", "status"]
ALLOWED_STATUSES = ["applied", "interview", "offer", "rejected"]


# Asks a question until the answer is not empty, and returns it without extra spaces
def ask_text(question):
    answer = input(question).strip()
    while answer == "":
        print("This cannot be empty.")
        answer = input(question).strip()
    return answer


# Asks for the date of the application; Enter means today, and a date that does not exist is refused
def ask_date(question):
    while True:
        answer = input(question).strip()
        if answer == "":
            return date.today().isoformat()
        try:
            return date.fromisoformat(answer).isoformat()
        except ValueError:
            print("Please type the date like 2026-11-17, or press Enter for today.")


# Asks for the status until it is one of the four allowed words (capitals are accepted)
def ask_status(question):
    answer = input(question).strip().lower()
    while answer not in ALLOWED_STATUSES:
        print("Please type one of: applied, interview, offer, rejected.")
        answer = input(question).strip().lower()
    return answer


# Adds one application at the end of the file ("a" mode, so earlier entries are kept).
# The header line is written only when the file does not exist yet or is still empty.
def save_entry(entry):
    file_is_new = not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        if file_is_new:
            writer.writerow(COLUMNS)
        writer.writerow(entry)


# Collects one application, saves it, and tells the user where it went
print("New internship application")
company = ask_text("Company: ")
position = ask_text("Position: ")
date_applied = ask_date("Date applied (YYYY-MM-DD, Enter for today): ")
status = ask_status("Status (applied, interview, offer, rejected): ")
save_entry([company, position, date_applied, status])
print("Saved in", FILE_NAME)

# Check it yourself (what happened when I ran it):
# I ran the program five times with five different applications.
# internship_applications.csv now has 6 lines: 1 header line and 5 entries,
# so the header is written only once and each run added a line without overwriting the others.
# When I left the company empty, typed a date like 2026-13-45 or a status like "maybe", the program asked again.