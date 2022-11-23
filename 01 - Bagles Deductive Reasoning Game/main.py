"""Bagels - Deductive Logic Game"""

# Modules
import random


def setup_length():
    """
    Asks user to input 'length'. Checks input is valid and if not asks
    for input again until valid input is obtained.
    Returns: length (int)
    """
    while True:
        try:
            length = int(
                input(
                    "How many digits would you like to guess? [Enter length "
                    "as a numerical value] "
                )
            )
            return length
        except ValueError:
            print("You did not enter a numerical value.")


def setup_attempts():
    """
    Asks user to input 'attempts'. Checks input is valid and if not asks
    for input again until valid input is obtained.
    Returns: 'attempts' (int)
    """
    while True:
        try:
            attempts = int(
                input(
                    "How many guesses would you like? "
                    "[Enter a numerical value] "
                )
            )
            return attempts
        except ValueError:
            print("You did not enter a numerical value.")


def get_guess(target):
    """
    Asks user to input 'user_guess'. Checks input is valid and if not
    asks for input again until valid input obtained.
    Returns: 'user_guess' (str)
    """
    while True:
        user_guess = input(f"Enter {len(target)} Digit Number: ")
        if not user_guess.isdigit() or len(user_guess) != len(target):
            print(
                "Your entry must be a number and be be of a length equal to "
                "the target number."
            )
        else:
            return user_guess


def play_again():
    """
    Asks user to input 'yes' or 'no' for restart. Checks input is valid
    and if not asks again until it is.
    Returns: True or False (bool)
    """
    while True:
        restart = input(
            "Session Over.  Would you like to play again? ['Yes' or 'No'] "
        ).lower()
        if restart == "yes":
            return True
        elif restart == "no":
            return False
        else:
            print("You must answer 'Yes' or 'No' to continue.")


def main():
    """
    Game Logic
    """
    print(
        "Bagels - A deductive logic game.\nBy Nicolas.\n\n"
        "I will think of a digit sequence of user defined length.\n"
        "Each digit in the sequence will be a random value between "
        "between 0 - 9.\nIt is your job to then guess the sequence in a user "
        "defined number of tries or less.\nHere are some clues:\n\n"
        "When I say:\tThat means:\n"
        " Pico\t\tA digit is correct but in the wrong position.\n"
        " Fermi\t\tA digit is correct and in the right position.\n"
        " Bagels\t\tNo digit is correct.\n\n"
        "For example if the target sequence was 248 and your guess was 843, "
        "my clue would be 'Fermi Pico'.\nLet's play.\n\n"
    )
    playing = True
    while playing:
        target_length = setup_length()
        attempts_max = setup_attempts()
        target = ""
        for _ in range(target_length):
            num = str(random.randint(0, 9))
            target += num
        print(
            f"\nFor testing purposes, the sequence I am thinking of is: "
            f"{target}\n"
        )
        attempts = 1
        while attempts <= attempts_max:
            print(f"Guess #{attempts}")
            guess = get_guess(target)
            if guess == target:
                print("You got it!")
                break
            else:
                response = ""
                for index, number in enumerate(guess):
                    if target[index] == number:
                        response += "Fermi "
                    elif number in target:
                        response += "Pico "
                if not response:
                    print("Bagels")
                else:
                    print(response)
                attempts += 1
        playing = play_again()
    print("Game Over")


# If module is run as opposed to imported run 'main()'.
if __name__ == "__main__":
    main()
