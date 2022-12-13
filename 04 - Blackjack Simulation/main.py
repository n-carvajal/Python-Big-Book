"""Blackjack Simulations"""

# Imports
from deck import Deck
from player import Player


# Functions
def start_game():
    """
    Asks user if they want to play the game and validates their response
    to ensure it is either Y or N.
    Returns True if Y and False if N.
    """
    while True:
        play = input("\nWould you like to play?\nType (Y)es or (N)o: ").lower()
        if play == "n":
            return False
        elif play != "y":
            print("You did not enter (Y)es or (N)o.")
        else:
            print("OK. Let's begin...")
            return True


def deck_count():
    """
    Asks user how many decks they would like to play with and validates
    their response to ensure it is a number within the allowed range.
    Returns decks as an integer.
    """
    while True:
        decks = input("\nHow many decks would like to play with? (1-6): ")
        if decks.isdigit() and int(decks) > 0 and int(decks) < 7:
            return int(decks)
        else:
            print("You did not enter a number between 1 and 6.")


def start_cash():
    """
    Asks user how much cash they would like to start with in multiples
    of 100 and validates their response to ensure it is within the
    required parameter.
    Returns cash as an integer.
    """
    while True:
        cash = input(
            "\nHow much cash do you want to start with?\nEnter "
            "a number in multiples of $100: $"
        )
        if cash.isdigit() and int(cash) % 100 == 0:
            return int(cash)
        else:
            print("You did not enter a multiple of a $100 or a numeric value.")


def double_down():
    """
    Asks player if they would like to double down and validates their
    response.
    Returns True if 'y'
    Returns False if 'n'
    """
    while True:
        answer = input("\nDouble down? Type (Y)es or (N)o: ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("You did not enter (Y)es or (N)o.")


def hit():
    """
    Asks player if they would like to (H)it or (S)stand and validates
    their response to ensure they only enter 'H' or 'S'.
    Returns True if 'H'.
    Returns False if 'S'.
    """
    while True:
        answer = input("\nWould you like to (H)it or (S)tand: ").lower()
        if answer == "h":
            return True
        elif answer == "s":
            return False
        else:
            print("You did not enter (H)it or (S)tand.")


# Introduce Game.
print("\nWelcome to Blackjack 21")
print("by Nicolas Carvajal\n")
print("\tRules:")
print("\t\tTry to get as close to 21 without going over.")
print("\t\tKings Queens, and Jacks are wroth 10 points.")
print("\t\tAces are worth 1 or 11 points.")
print("\t\tCards 2 through 10 are worth their face value.")
print("\t\t(H)it to take another card.")
print("\t\t(S)tand to stop taking cards.")
print(
    "\t\tOn your first play you can double down to increase your bet but"
    "must hit exactly one more time before standing."
)
print("\t\tIn case of a tie, the bet is returned to the player.")
print("\t\tThe dealer must hit if their hand is less than 17.")

# Ask to start game.
if start_game():

    # Ask how many decks to play with.
    game_decks = deck_count()

    # Ask how much money they would like to play with.
    bankroll = start_cash()

    # TODO Ask for replay after X rounds if winning Y if losing.

    # Deck and Player class instantiation.
    shoe = Deck()
    player = Player("Nico", bankroll)
    house = Player("House", bankroll)

    # Setup number of decks in shoe.
    for _ in range(game_decks):
        shoe.create()

    # Shuffle shoe.
    shoe.shuffle()

    # Set game bet amount.
    bet_amount = bankroll / 10

    # Introduce player and house.
    print("\nOK let's start.")
    print(player)
    print(house)
    print(f"The game bet amount is set at: ${round(bet_amount)}")
    print("Bets are placed, let's deal...\n")

    # Have player and house place bets.
    bet = player.bet(bet_amount) + house.bet(bet_amount)

    # Have player and house gather 2 dealt cards from shoe.
    player.gather_hand(shoe.deal(2))
    house.gather_hand(shoe.deal(2))

    # Show and score player and house hands
    print(f"{player.name} has: ")
    player.show_hand()
    player.score_hand()
    print(f"{house.name} has: ")
    house.show_hand(show_all=False)
    house.score_hand()

    # Ask if player if they would like to double down.
    if double_down():

        # Increase bet for player and house.
        bet += player.bet(bet_amount) + house.bet(bet_amount)

        # Deal extra card to player, have player gather and score player hand.
        player.gather_hand(shoe.deal(1))
        player.score_hand()

        # Show hands again.
        print(f"\n{player.name} has: ")
        player.show_hand()
        print(f"{house.name} has: ")
        house.show_hand(show_all=False)

        # TODO: Use while loop to ask hit or miss?
        # Check if player still in game.
        if player.score_hand() > 21:
            house.collect_winnings(bet)
            print("Sorry you are bust.")
        else:
            if hit():
                pass

    else:
        print("NO")

    # if player.score_hand() == house.score_hand():
    #     player.collect_winnings(round(bet/2))
    #     house.collect_winnings(round(bet/2))
    # elif player.score_hand() > house.score_hand():
    #     player.collect_winnings(bet)
    # else:
    #     house.collect_winnings(bet)

    # print(player)
    # print(house)
else:
    print("Game Over")

# import random

# card_suits = {
#     "Hearts": chr(9829),
#     "Diamonds": chr(9830),
#     "Spades": chr(9824),
#     "Clubs": chr(9827),
# }
# card_values = {
#     "2": 2,
#     "3": 3,
#     "4": 4,
#     "5": 5,
#     "6": 6,
#     "7": 7,
#     "8": 8,
#     "9": 9,
#     "10": 10,
#     "J": 10,
#     "Q": 10,
#     "K": 10,
#     "A": 11,
# }

# # Setup deck.
# deck = []
# for suit in card_suits.values():
#     for rank, value in card_values.items():
#         card = {f"{rank}{suit}": value}
#         deck.append(card)

# # Shuffle deck.
# random.shuffle(deck)

# # Setup players.
# player_hand = []
# player_display = []
# player_value = 0
# house_hand = []
# house_display = []
# house_value = 0

# # Deal 2 cards to each player.
# for _ in range(2):
#     player_hand.append(deck.pop())
# for _ in range(2):
#     house_hand.append(deck.pop())

# # Calculate player display and value.
# for card in player_hand:
#     for display, value in card.items():
#         player_display.append(display)
#         player_value += value

# # Show player display and value.
# # print(player_hand)
# print()
# print(f"Player's hand: {player_display}")
# print(f"Player's hand value: {player_value}")
# print()

# # Calculate house display and value.
# for card in house_hand:
#     for display, value in card.items():
#         house_display.append(display)
#         house_value += value

# # Show house display and value.
# # print(house_hand)
# print(f"House's hand: {house_display[0]}")
# print(f"House's hand value: {house_value}")
# print()

# # Check deck length.
# print(f"Cards Remaining: {len(deck)}")
# print()

# # Game loop
# while True:
#     # Ask if player wants to hit or stick.
#     answer = input("Do you want to 'stay' or would you like a 'hit': ")

#     # If player hits.
#     if answer == "hit":

#         # Deal 1 card to player.
#         player_hand.append(deck.pop())

#         # Calculate player display and value.
#         for display, value in player_hand[-1].items():
#             player_display.append(display)
#             player_value += value

#         # Show player display and value.
#         print(f"Player's hand: {player_display}")
#         print(f"Player's hand value: {player_value}")
#         print()

#         # Check player is not bust.
#         if player_value > 21:
#             print("BUST")
#             break
#         else:
#             # Show house display and value.
#             print(f"House still has: {house_display[0]}")
#             print(f"House's hand value: {house_value}")
#             print()

#         # Check deck length.
#         print(f"Cards Remaining: {len(deck)}")

#     # If player sticks.
#     elif answer == "stick":

#         # Show player display and value.
#         print(f"Player's hand: {player_display}")
#         print(f"Player's hand value: {player_value}")
#         print()

#         # Show house full hand.
#         print(f"House still has: {house_display}")
#         print(f"House's hand value: {house_value}")
#         print()

#         # If house_value less than 17.
#         if house_value < 17:

#             # Deal card to house_hand
#             house_hand.append(deck.pop())

# print("GAME OVER")
