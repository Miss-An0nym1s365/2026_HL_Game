import math


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
secret number will be between 1 and 100).

Then you must choose how many rounds you'd like to play, 
select <enter> for infinite mode.

Your end goal is to try to guess the 🔐secret🔐 number 
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
                 f"is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinte mode / exit code
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

print("⬆️⬆️⬆️Welcome to the Higher Lower Game!⬇️⬇️⬇️")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

#Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter> for infinite mode: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# get game parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num+1)
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

    # get user choice
    user_choice = input("Choose: ")

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area