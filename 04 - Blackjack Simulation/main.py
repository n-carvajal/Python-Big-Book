"""Blackjack Simulations"""

# Imports
from deck import Deck
from player import Player

# Deck and Player class instantiation
shoe = Deck()
player = Player("Nico", 1000)
house = Player("House", 1000)

# Setup number of decks in shoe
shoe_decks = 6
for _ in range(shoe_decks):
    shoe.create()

# Shuffle shoe
shoe.shuffle()

# Have player and house gather 2 dealt cards from shoe.
player.gather_hand(shoe.deal(2))
house.gather_hand(shoe.deal(2))

# Show player and house hands
player.show_hand()
house.show_hand(show_all=False)

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
