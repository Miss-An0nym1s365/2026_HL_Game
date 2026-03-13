# functions go here

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
def int_check(question):
    """Checks users enter an integer more than / equal to 1"""
    while True:
        error = "Please enter an integer more than / equal to 1"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"


        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

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
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

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