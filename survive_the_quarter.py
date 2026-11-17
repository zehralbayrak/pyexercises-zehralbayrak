# Name: Zehra Albayrak | Group: B
#
# 1. What goes in: my group's file scenarios_B.csv (one situation per line with options A, B and C,
#    each with a text, a money change, a reputation change and a reaction), then from the keyboard
#    the player's name, the difficulty (e or h) and one letter A, B or C per day.
#    The separator is a semicolon (;) and there are 14 columns: Num, Situation, then four columns per option
#    (A_Choice, A_Money, A_Buzz, A_Reaction, and the same for B and C). The numbers are whole numbers,
#    negatives have a minus sign and there is no thousands separator. The impact of option B is in B_Money and B_Buzz.
# 2. What happens (one day, in order, one line each): 
#    - The day number, the budget, the reputation, the situation and the three options are shown.
#    - The player types A, B or C, and the program asks again until the answer is valid.
#    - The option's money change is added to the budget and its reputation change to the reputation (max 100).
#    - The reaction is printed with both changes, for example "Budget -1000 EUR, Reputation +5".
#    - The day goes into the history as (reputation change, day, option text).
#    - If the budget or the reputation is 0 or less, the player is fired and the game stops.
#      If not, the next day starts.
# 3. What comes out: 
#    on the screen, "FIRED" with the reason, or the final score (reputation + 1 point per 200 EUR left) with the title, then the best and the worst move of the game. 
#    One line (name, budget, reputation, title, date) is added to results.csv.
# 4. What could go wrong (at least three things, and what my program does): 
#    - The player types something other than A, B or C: the program asks again (lower case and spaces are fine).
#    - The player types something other than e or h for the difficulty: the program asks again.
#    - The player leaves the name empty: the name becomes "Player".
#    - scenarios_B.csv is not in the folder: a message is printed and the game ends without a Python error.
#    - A line of the file has an empty column or a Money or Buzz value that is not a number: that line is
#      skipped with its line number and the game uses the other lines (a decimal comma like 2,5 is accepted).
#    - The file has fewer than 10 scenarios: the player is told and the quarter is shorter.
#    - results.csv cannot be written (for example it is open in Excel): a message says the game was not saved.
#    - The player presses Ctrl+C or Ctrl+D: the game stops with a short message instead of an error.
#
# Feature chosen: (d) Difficulty
# Why: with 15000 EUR on easy the player can try the expensive options and still survive. With 6000 EUR
#    on hard a few costly choices are enough to get fired, so money has to be watched as much as reputation.
#    The budget left also counts in the score, so a good title is harder to get on hard.
#    In the code it only needs one dictionary and one extra question at the start.

import csv
import os
import random
from datetime import date

# Game settings from the brief, kept in one place so they are easy to check and change
SCENARIO_FILE = "scenarios_B.csv"
RESULTS_FILE = "results.csv"
STARTING_REPUTATION = 50
MAX_REPUTATION = 100
DAYS_PER_GAME = 10

# Feature (d): each difficulty letter gives a different starting budget
DIFFICULTY_BUDGETS = {"e": 15000, "h": 6000}

# The three letters the player can type, and the position of that option in the list
CHOICE_POSITIONS = {"A": 0, "B": 1, "C": 2}


# Turns a number written as text in the file into a whole number of euros or points.
# A decimal comma is accepted (European style). Empty or non-numeric text raises ValueError.
def text_to_number(text):
    if text is None or text.strip() == "":
        raise ValueError("missing number")
    cleaned = text.strip().replace(",", ".")
    return int(round(float(cleaned)))


# Builds one option as a tuple (text, budget_change, reputation_change, feedback)
# from the four columns of its letter, for example B_Choice, B_Money, B_Buzz and B_Reaction.
def read_option(row, letter):
    text = row[letter + "_Choice"]
    feedback = row[letter + "_Reaction"]
    if text is None or feedback is None or text.strip() == "" or feedback.strip() == "":
        raise ValueError("missing text")
    budget_change = text_to_number(row[letter + "_Money"])
    reputation_change = text_to_number(row[letter + "_Buzz"])
    return (text.strip(), budget_change, reputation_change, feedback.strip())


# Reads every scenario of my group's file and returns a list of (situation, [option A, option B, option C]).
# A row with a missing column or a bad number is skipped with a message, so one broken line cannot stop the game.
def load_scenarios(filename):
    scenarios = []
    try:
        with open(filename, newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=";")
            for line_number, row in enumerate(reader, start=2):
                try:
                    situation = row["Situation"]
                    if situation is None or situation.strip() == "":
                        raise ValueError("missing situation")
                    options = []
                    for letter in CHOICE_POSITIONS:
                        options.append(read_option(row, letter))
                    scenarios.append((situation.strip(), options))
                except (KeyError, ValueError, OverflowError):
                    print("Skipping line", line_number, "of", filename, "(missing column or bad number)")
    except FileNotFoundError:
        print("Could not find", filename, "- it must be in the same folder as this program.")
    return scenarios


# Asks the player's name. An empty answer becomes "Player" so results.csv never has a blank name.
def ask_name():
    name = input("Your name: ").strip()
    if name == "":
        name = "Player"
    return name


# Feature (d): asks easy or hard until the answer is e or h (any case, spaces ignored)
# and returns the starting budget of that level.
def ask_difficulty():
    while True:
        answer = input("Difficulty: (e)asy 15000 EUR or (h)ard 6000 EUR? ").replace(" ", "").lower()
        if answer in DIFFICULTY_BUDGETS:
            return DIFFICULTY_BUDGETS[answer]
        print("Please type e or h.")


# Shows everything the manager needs to decide: the day, both gauges, the situation and the three options.
def show_day(day, budget, reputation, situation, options):
    print()
    print("--- Day", day, "---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/{MAX_REPUTATION}]")
    print(situation)
    print("   A:", options[0][0])
    print("   B:", options[1][0])
    print("   C:", options[2][0])


# Asks A, B or C until the answer is valid (lower case and spaces accepted)
# and returns the position of the chosen option: 0, 1 or 2.
def ask_choice():
    answer = input("Your choice (A, B or C): ").replace(" ", "").upper()
    while answer not in CHOICE_POSITIONS:
        answer = input("Please type A, B or C: ").replace(" ", "").upper()
    return CHOICE_POSITIONS[answer]


# Applies the money and reputation impact of the chosen option and returns both new gauges as a tuple.
# Reputation can never go above 100, but the budget has no ceiling.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation


# Explains why the player is fired, or returns "" if both gauges are still above 0.
def get_fired_reason(budget, reputation):
    if budget <= 0 and reputation <= 0:
        return "the budget and the reputation both fell to 0 or less"
    elif budget <= 0:
        return "the budget fell to 0 or less"
    elif reputation <= 0:
        return "the reputation fell to 0 or less"
    return ""


# Plays up to 10 days and stops at once if the player is fired.
# Each day goes into the history as (reputation_change, day, option_text): reputation change comes first
# because Python compares tuples element by element, so max() and min() then find the best and worst move.
def play_game(scenarios, budget, reputation):
    history = []
    fired_reason = ""
    days = min(DAYS_PER_GAME, len(scenarios))
    for day in range(1, days + 1):
        situation, options = scenarios[day - 1]
        show_day(day, budget, reputation, situation, options)
        option = options[ask_choice()]
        budget, reputation = apply_choice(budget, reputation, option)
        text, budget_change, reputation_change, feedback = option
        print(feedback)
        print(f"Budget {budget_change:+} EUR, Reputation {reputation_change:+}")
        history.append((reputation_change, day, text))
        fired_reason = get_fired_reason(budget, reputation)
        if fired_reason != "":
            break
    return budget, reputation, history, fired_reason


# Final score from the brief, only for players who survive: reputation plus 1 point per 200 EUR left.
def compute_score(budget, reputation):
    return reputation + budget // 200


# Turns the final score into the title from the brief's table.
def get_title(score):
    if score >= 140:
        return "Viral Legend"
    elif score >= 120:
        return "CMO Material"
    elif score >= 95:
        return "Growth Hacker"
    else:
        return "Eternal Intern"


# Returns the days with the biggest and the smallest reputation change, as a tuple (best, worst).
def find_best_and_worst_moves(history):
    return max(history), min(history)


# Appends one line per game to results.csv so every player leaves a trace.
# The column names are written only when the file does not exist yet.
def save_result(name, budget, reputation, title):
    file_is_new = not os.path.exists(RESULTS_FILE)
    try:
        with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file_is_new:
                writer.writerow(["name", "budget", "reputation", "title", "date"])
            writer.writerow([name, budget, reputation, title, date.today().isoformat()])
        print("Saved in", RESULTS_FILE)
    except OSError:
        print("Could not write", RESULTS_FILE, "- this game was not saved.")


# Runs one full game: setup, the days, the result, the best and worst move, and the saved line.
def main():
    print("=== SURVIVE THE QUARTER: Croissant Rocket ===")
    scenarios = load_scenarios(SCENARIO_FILE)
    if len(scenarios) == 0:
        print("No scenarios to play. Goodbye.")
        return
    if len(scenarios) < DAYS_PER_GAME:
        print("Only", len(scenarios), "scenarios found, so this quarter is shorter.")
    name = ask_name()
    budget = ask_difficulty()
    reputation = STARTING_REPUTATION
    random.shuffle(scenarios)

    budget, reputation, history, fired_reason = play_game(scenarios, budget, reputation)

    # The result: fired and why, or the score and the title
    print()
    print("=" * 30)
    if fired_reason != "":
        title = "Fired"
        print(f"You are FIRED, {name}: {fired_reason}.")
        print(f"Budget: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
    else:
        score = compute_score(budget, reputation)
        title = get_title(score)
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print("Final score:", score)
        print(f"{name}, your title: {title}")

    # The best and worst move, so the player sees which decisions mattered most
    best, worst = find_best_and_worst_moves(history)
    print(f'Best move:  day {best[1]}, "{best[2]}" ({best[0]:+})')
    print(f'Worst move: day {worst[1]}, "{worst[2]}" ({worst[0]:+})')

    save_result(name, budget, reputation, title)


# Starts the game. Ctrl+C or Ctrl+D ends it politely instead of showing a Python error.
try:
    main()
except (KeyboardInterrupt, EOFError):
    print()
    print("Game stopped by the player. Nothing was saved.")
