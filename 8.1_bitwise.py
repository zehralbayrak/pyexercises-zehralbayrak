"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: four permissions on a monthly financial report, each stored as one bit:
#    VIEW (read the report), EDIT (change the figures), APPROVE (sign off the figures)
#    and SEND (send the report to management)
# 2. Process: the program gives an intern VIEW and EDIT by combining them with |, tests with &
#    whether SEND is already there, adds SEND with |, then removes EDIT with & and ~ once the report is sent
# 3. Out: one line per step with the value in binary and the names of the permissions that are on
# 4. What my permissions are about: who may do what on the monthly reporting file in a finance team.
#    An intern can prepare the figures, only a manager approves them, and once the report has been sent
#    nobody should be able to edit the figures any more.

# Your code below

# The four permissions, one bit each, from right to left
VIEW = 0b0001     # can open and read the report
EDIT = 0b0010     # can change the figures
APPROVE = 0b0100  # can sign off the figures
SEND = 0b1000     # can send the report to management

PERMISSION_NAMES = [("SEND", SEND), ("APPROVE", APPROVE), ("EDIT", EDIT), ("VIEW", VIEW)]


# Prints one step: its label, the value as 4 bits, and the names of the permissions that are on
def show_step(label, permissions):
    names = []
    for name, bit in PERMISSION_NAMES:
        if permissions & bit:
            names.append(name)
    if len(names) == 0:
        names.append("nothing")
    print(f"{label:<34}{permissions:04b}   {', '.join(names)}")


# Step 1: combine two permissions with | (bitwise OR): the intern can read and edit the report
intern = VIEW | EDIT
show_step("1. Intern gets VIEW | EDIT", intern)

# Step 2: test with & (bitwise AND) whether a third permission is already there
has_send = (intern & SEND) != 0
show_step("2. intern & SEND", intern & SEND)
print("   Can the intern send the report?", has_send)

# Step 3: add the third permission with |: the intern may now send the report to management
intern = intern | SEND
show_step("3. Add SEND with |", intern)

# Step 4: remove one permission with & and ~ (NOT): after sending, the figures are locked
intern = intern & ~EDIT
show_step("4. Remove EDIT with & ~", intern)

# Check it yourself (what happened when I ran it):
# Step 1 shows 0011: the two bits on the right are on, VIEW and EDIT.
# Step 2 shows 0000: 0011 & 1000 has no bit in common, so the intern cannot send yet (False).
# Step 3 shows 1011: the SEND bit on the left is now on as well.
# Step 4 shows 1001: the EDIT bit is off again, and only VIEW and SEND are left. I read the same bits myself.
