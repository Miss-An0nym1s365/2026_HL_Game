import math
import random


# checks user enter yes (y) or no (n)

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y /
        if response =="yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

To begin, choose the number of rounds and either customise 
the game parameters or go with the default game (where the
secret number will be between 1 and 10).

Then you must choose how many rounds you'd like to play, 
select <enter> for infinite mode.

Your end goal is to try to guess the 🤫secret🤫 number 
without running out of guesses.

Good luck player 🤝
    """)

# checks for
def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number neds to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f"more than / equal to {low}")

    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the integer not too high or low
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                 return response

        except ValueError:
            print(error)

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = [0]
all_scores = [0]
best_score = [1]
worst_score = [-1]
average_score = []

print("⬆️⬆️⬆️Welcome to the Higher Lower Game!⬇️⬇️⬇️")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

#Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter> for infinite mode: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# ask user if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose the high / low number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num+1)

# calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} (Infinite Mode)♾♾♾"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)
    print()

    # round starts here
    # set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num, high_num)
    print("Spoiler Alert", secret)      #remove this line after testing

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask user to guess the number
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check that they don't want to quit
        if guess == "xxx":
            # set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        # check that guess is not duplicate
        if guess in already_guessed:
            
            print(f"You've already guesses {guess}. You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

            #  if guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        guesses_used += 1

        # If we have guesses left...
        if guess < secret and guesses_used < guesses_allowed:
            feedback = ("Too low, please try a higher number."
                        f"You've used {guesses_used} / {guesses_allowed} guesses ")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = ("Too high, please try a lower number."
                        f"You've used {guesses_used} / {guesses_allowed} guesses ")
        elif guess == secret:

            if guesses_used == 1:
                feedback = "🍀🍀 Lucky! You got it on the first guess. 🍀🍀"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses."
            else:
                feedback = f" Well done! you guessed the secret number in {guesses_used} guesses!"
        else:
            feedback = f"Sorry you have no more guesses, the secret number was {secret}. YOU LOSE HAHA 🫵😂"

        # print feedback to user
        print(feedback)

        # additional feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1:
            print("\n💣💣💣Careful - you have one guess left!💣💣💣\n")

    print()
    print("End of round")


    print()

    # round ends here

    # if user has entered exit code, end game!
    if end_game == "yes":
        break

    rounds_played += 1
    user_choice = "guess"

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break


    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here
# before calculating statistics
if rounds_played > 0:
    # Game History / Statistics area

    # calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # output statistics
    print("\n📊📊📊 Statistics 📊📊📊")
    print(f"Best:{best_score} | Worst:{worst_score} | Average:{average_score:.2f} ")

    # display the game history on request
    see_history = yes_no("Do you wanna see ur game history? ")
    if see_history =="yes":
        for item in game_history:
            print(item)