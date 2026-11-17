"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - The capitals are mixed: some names are all in capitals ("LOVELACE", "GUIDO"), others all in lower case ("grace hopper")
# - Some lines start with spaces ("  alan TURING", "  linus torvalds")
# - There are empty lines in the file (line 3 and line 9)
# - One name has three words instead of two ("GUIDO van rossum"), so the last name is not simply the second word


# 1. In: names.txt, a text file with one person per line (first name, then last name), 10 lines in total
# 2. Process, problem by problem: 
#    - Mixed capitals: each word gets a capital first letter and the rest in lower case ("ada LOVELACE" becomes
#      "Ada Lovelace"), except "van", which stays in lower case because it is part of a Dutch last name
#    - Spaces at the start: strip() removes the spaces at the start and the end of each line before anything else
#    - Empty lines: after strip() an empty line becomes "", so the program skips it
#    - Three words: the first word is the first name and the rest stays together ("van Rossum"), but the
#      sorting uses only the last word (see answer 4)
# 3. Out: a new file, names_sorted.txt, with the 8 clean names, one per line, sorted by last name.
#    names.txt is only opened for reading, so it stays exactly as it was.
# 4. How I decide which word is the last name: with two words, the first is the first name and the second is the
#    last name. With three words ("Guido van Rossum"), "van" belongs to the last name but the family name itself is
#    Rossum. In the Netherlands, names like this are sorted under the main name (R), so I sort by the last word.


# Your code below

INPUT_FILE = "names.txt"
OUTPUT_FILE = "names_sorted.txt"

# Small words that belong to a last name and stay in lower case, like "van" in Guido van Rossum
LOWERCASE_PARTICLES = ["van", "von", "de", "der", "da", "di", "du", "le", "la"]


# Fixes the capitals of one name: capital first letter for each word, except particles like "van"
def fix_capitals(name):
    words = name.split()
    fixed_words = []
    for position, word in enumerate(words):
        if position > 0 and word.lower() in LOWERCASE_PARTICLES:
            fixed_words.append(word.lower())
        else:
            fixed_words.append(word.capitalize())
    return " ".join(fixed_words)


# Reads names.txt and returns the clean names: spaces removed, empty lines skipped, capitals fixed.
# The file is opened with "r" (read only), so the original is never changed.
def load_clean_names(filename):
    names = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned == "":
                continue
            names.append(fix_capitals(cleaned))
    return names


# Returns what the sorting looks at: the last word of the name, in lower case so capitals cannot change the order
def last_name_key(name):
    return name.split()[-1].lower()


# Writes the names to a new file, one per line ("w" creates the file, or replaces an older output)
def save_names(names, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")


# Main part: load and clean, sort by last name, save, then print the numbers I need for the check
names = load_clean_names(INPUT_FILE)
sorted_names = sorted(names, key=last_name_key)
save_names(sorted_names, OUTPUT_FILE)

# Counting the lines of the original file, empty ones included, to compare with the output
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    input_line_count = len(file.readlines())

print("Lines in", INPUT_FILE + ":", input_line_count)
print("Names in", OUTPUT_FILE + ":", len(sorted_names))
print("First in the list:", sorted_names[0])
print("Last in the list:", sorted_names[-1])

# Check it yourself (what happened when I ran it):
# names.txt has 10 lines and names_sorted.txt has 8, because the 2 empty lines (line 3 and line 9) were skipped.
# Checked by hand: the first name is Margaret Hamilton (H is the first last-name letter in the list)
# and the last one is Alan Turing (Turing comes after Torvalds because "tu" comes after "to").
# Guido van Rossum is sorted under R, between Lovelace and Torvalds, as I decided in answer 4.
# names.txt looks exactly the same as before, so the original file was not modified.