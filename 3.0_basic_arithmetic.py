"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers typed by the user; input() gives text, so float() turns them into numbers that can have decimals 
# 2. Process: the program adds, subtracts, multiplies, and divides the two numbers
# 3. Out: four results printed on screen, one line for each operation
# 4. What happens when the second number is zero, and why: the program shows a message instead of the division result, so the user still gets the other three results and the program does not crash


# Your code below

# asks for two numbers; float() turns the typed text into numbers that can have decimals
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# adding the two numbers
total = number_1 + number_2

print("The total of two numbers is:", total)


# difference of the two numbers
difference = number_1 - number_2
print("The difference between the two numbers is:", difference)


# multiplication of two numbers
product = number_1 * number_2
print("The product of two numbers is:", product)


# my decision for zero: show a message instead of dividing, so the program does not crash
if number_2 != 0:
    division = number_1 / number_2
    print("The division of two numbers is:", division)
else:
    print("The number 2 that you have entered is zero")


# test (what happened when I ran it):
# 7 and 2: in my head 7 / 2 = 3.5, and the program also showed 3.5
# it did not show 3 because / keeps the decimals; // would drop them and give 3
# the other results end in .0 (9.0, 5.0, 14.0) because float() turns the numbers into decimal numbers
# 34 and 0: the program showed the total, difference and product, then my message instead of the division