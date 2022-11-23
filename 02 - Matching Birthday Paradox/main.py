"""Birthday Paradox"""

# Imports
import random
import datetime


def birthday_generator(size):
    """
    Takes in 'size' and creates a random birthday list of 'size' called
    'birthdays'. First it creates an empty list called 'birthdays' and
    then it starts a loop for 'range(size)' on every loop it sets
    'start_date' as 01/01/1980 then proceeds to add a random number of
    days 'random_days' to 'start_date' the result is labelled 'birthday'
    and is appended to 'birthdays list.
    Args: 'size' (int): Sample size obtained from user.
    Returns: 'birthdays' (list)
    """
    birthdays = []
    for _ in range(size):
        start_date = datetime.date(1980, 1, 1)
        random_days = datetime.timedelta(days=random.randint(0, 364))
        birthday = start_date + random_days
        birthdays.append(birthday)
    return birthdays


def get_birthday_count():
    """
    Gets number of birthdays to generate, ensure the input is numerical
    and between 0 - 100. If not then asks again.
    Returns: 'sample_size' (int)
    """
    while True:
        sample_size = input(
            "How many birthdays would you like to generate? (Max 100)\n>"
        )
        if sample_size.isdigit() and 1 < int(sample_size) <= 100:
            return int(sample_size)
        else:
            print(
                "You must enter a numerical value between 2 - 100 inclusive."
            )


def get_simulation_count():
    """
    Gets number of simulations to run, ensure the input is numerical and
    between 0 - 200. If not then asks again.
    Returns: 'simulation_size' (int)
    """
    while True:
        simulation_size = input(
            "\nHow many '000s of simulations would you like to run? "
            "(Enter 0 - 200):\n>"
        )
        if simulation_size.isdigit() and 0 < int(simulation_size) <= 200:
            return int(simulation_size)
        else:
            print("You must enter a numerical value between 1 - 200.")


def main():
    """Runs Birthday Paradox"""
    print(
        "Birthday Paradox, by Nicolas Carvajal\n\nThe Birthday Paradox shows "
        "us that in a group of 'N' people, the odds that two of them have "
        "matching birthdays is surprisingly large.\nThis script performs a "
        "Monte Carlo simulation, that is repeated random simulations, to "
        "explore this concept.\n\nLet it be noted it is not actually a "
        "'paradox' just a surprising result.\n"
    )
    birthdays_count = get_birthday_count()
    birthdays_list = birthday_generator(birthdays_count)
    birthdays_formatted = ""
    for date in birthdays_list:
        birthdays_formatted += f"{date.strftime('%d')} {date.strftime('%b')}, "
    print(
        f"Here is your list of {birthdays_count} birthdays:\n\n"
        f"{birthdays_formatted.rstrip(', ')}\n\n"
    )
    duplicates_list = []
    for date in birthdays_list:
        if birthdays_list.count(date) > 1:
            duplicates_list.append(date)
    if not duplicates_list:
        print("Your list contains no matching birthdays.\n")
    else:
        duplicates_set = set(duplicates_list)
        duplicates_formatted = ""
        for date in duplicates_set:
            duplicates_formatted += (
                f"{date.strftime('%d')} {date.strftime('%b')}, "
            )
        print(
            f"In your list multiple people have birthdays on: "
            f"{duplicates_formatted.rstrip(', ')}.\n"
        )
    print(
        f"Let's now perform a Monte Carlo simulation on some additional groups"
        f" of {birthdays_count} random birthdays and check for duplicates."
    )
    simulations = get_simulation_count()
    input(f"Press enter to start your {simulations * 1000} simulations...")
    text_substitution = 1
    simulation_tally = 0
    for _ in range(simulations * 1000):
        if _ % 1000 == 0:
            print(f"{text_substitution}0000 simulations completed.")
            text_substitution += 1
        birthdays_list = birthday_generator(birthdays_count)
        duplicates_list = []
        for date in birthdays_list:
            if birthdays_list.count(date) > 1:
                duplicates_list.append(date)
        if duplicates_list:
            simulation_tally += 1
    print(
        f"\nOf the {simulations * 1000} samples generated there were "
        f"duplicates in {simulation_tally} of them.\nTherefore there is a "
        f"{round((simulation_tally/(simulations * 1000)) * 100, 2)}% chance "
        f"of at least 2 people having matching birthdays in a group of "
        f"{birthdays_count} people.\n"
    )


# If module is run as opposed to imported run program.
if __name__ == "__main__":
    main()
