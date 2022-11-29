"""Blackjack Simulations"""

# Imports
from deck import Deck
from player import Player

# TODO Introduce Game.
# TODO Ask how many decks to use.
# TODO Ask size of bet.
# TODO Ask for replay after X rounds if winning Y if losing.

# Deck and Player class instantiation
shoe = Deck()
player = Player("Nico", 1000)
house = Player("House", 1000)

# Setup number of decks in shoe
decks_in_play = 6
for _ in range(decks_in_play):
    shoe.create()

# Shuffle shoe
shoe.shuffle()

# Established bet amount.
bet_amount = 10

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

if player.score_hand() == house.score_hand():
    player.collect_winnings(round(bet/2))
    house.collect_winnings(round(bet/2))
elif player.score_hand() > house.score_hand():
    player.collect_winnings(bet)
else:
    house.collect_winnings(bet)

print(player)
print(house)

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
