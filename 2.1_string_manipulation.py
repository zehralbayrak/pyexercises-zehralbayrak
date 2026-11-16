"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's sentence, typed on the keyboard; Python stores it as a string
# 2. Process: the input is converted into 4 different versions 
# 3. Out: 4 sentences printed on screen showing the user's sentence in different versions
# 4. My four transformations, and when each is useful:
# - upper(): useful when text needs to stand out or follow a standard format, like a headline or a product code
# - lower(): useful when comparing text like email addresses, because making every letter small avoids mistakes caused by capitals
# - title(): useful when fixing a list of names quickly, because it gives each word a capital first letter without editing them one by one
# - replace(): useful when checking text for extra spaces, because every space becomes a visible underscore

# Your code below

# asks the user to type a sentence and program keeps it to use it in the transformation process
sentence = input("Type a sentence: ")

# makes four different versions of the sentence: all capital, all lowercase, each word capitalized, and spaces replaced by underscores
result1 = sentence.upper()
result2 = sentence.lower()
result3 = sentence.title()
result4 = sentence.replace(" ", "_")

# shows the result with the new version, so the user knows the transformation
print("upper():", repr(result1))
print("lower():", repr(result2))
print("title():", repr(result3))
print("replace():", repr(result4))

# test:
# sentence I used: " This is not my FiRST time using PYThon. "
# upper(): expected all letters in capitals, got ' THIS IS NOT MY FIRST TIME USING PYTHON. ', as expected? yes
# lower(): expected all letters in lowercase, got ' this is not my first time using python. ', as expected? yes
# title(): expected the first letter of each word in capitals, got ' This Is Not My First Time Using Python. ', as expected? partly, it also changed the letters in the middle into lowercase
# replace(): expected every space replaced by "_", got '_This_is_not_my_FiRST_time_using_PYThon._', as expected? yes