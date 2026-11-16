"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one invoice described in a dictionary with six fields, written in the code
# 2. Process: the program reads the amount, changes the status to paid, removes the reminder and shows every field
# 3. Out: the amount, then every remaining field with its value, one per line
# 4. My object, my five fields, and why those: an invoice; number (to find it), client (who pays), amount (how much), due date (when the money should arrive), status (paid or not), plus a reminder that I remove once the invoice is paid


# Your code below

# One invoice described with six fields
invoice = {
    "number": 1043,
    "client": "Dupont SARL",
    "amount": 2400,
    "due_date": "2026-10-31",
    "status": "unpaid",
    "reminder": "Call the client on 25 October",
}

# Reading one field: how much the client has to pay
print("Amount to pay:", invoice["amount"])

# Changing a field: the client has paid, so the status becomes "paid"
invoice["status"] = "paid"

# Removing a field: the invoice is paid, so the reminder is no longer needed
invoice.pop("reminder")

# Showing every field with its value, one per line
for field, value in invoice.items():
    print(field, ":", value)

# Asking for a field that does not exist: get() gives a message instead of crashing
print("Discount:", invoice.get("discount", "no such field"))


# test (what happened when I ran it):
# with print(invoice["discount"]), the program stopped with KeyError: 'discount', because that field does not exist
# with invoice.get("discount", "no such field"), the program showed "no such field" and did not crash
# the status changed to "paid" and the reminder no longer appears in the list of fields