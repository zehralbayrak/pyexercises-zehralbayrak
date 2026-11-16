"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the client's name and the last invoice number, typed by the user; Python stores both as strings
# 2. Process: the invoice number is turned into a number, 1 is added, and both go into one sentence
# 3. Out: one sentence showing the client's name and their next invoice number 
# 4. My two fields, and what I would do with them: client name and last invoice number, to get the next invoice number automatically and avoid duplicates


# Your code below

# asks for the client's name and the last invoice number
client_name = input("Enter the client's name: ")
last_invoice = input("Enter the last invoice number: ")

# input() always gives text, so adding 1 directly caused a TypeError; int() turns it into a number
invoice_number = int(last_invoice)

# adds 1 to get the next invoice number
next_invoice = invoice_number + 1

# shows one sentence with the client's name and the next invoice number
print("The client name is " + client_name + " and the client's next invoice number is", next_invoice)

# test (what happened when I ran it):
# empty line: ValueError, int() cannot turn an empty text into a number
# a space: ValueError, a space is not a number either, so int() fails the same way
# text instead of a number (abc): ValueError, int() cannot turn letters into a number
# in all three cases the program stops at the int() line