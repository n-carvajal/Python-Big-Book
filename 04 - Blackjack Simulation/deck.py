"""Deck Class"""

import random

import data


class Card:
    """
    Card class and its associated attributes and methods.
    """

    def __init__(self, rank, suit, value):
        """
        Defines Card object attributes upon instantiation.
        """
        self.face = f"{rank}{suit}"
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        """
        Returns print string for Card object.
        """
        return self.face


class Deck:
    """
    Deck class and its associated attributes and methods.
    """

    def __init__(self):
        """
        Defines Deck object attributes upon instantiation.
        """
        self.all_cards = []

    def create(self):
        """
        Creates 52 card deck.

        Creates a Card object for every 'suit' and 'rank' item in 'data'
        then appends that object to the 'self.all_cards' attribute of
        the Deck object.
        """
        for suit in data.card_suits.values():
            for rank, value in data.card_values.items():
                card = Card(rank, suit, value)
                self.all_cards.append(card)

    def shuffle(self):
        """
        Shuffles a deck of cards.

        Shuffles the Card objects in the 'self.all_cards' attribute of
        the Deck object.
        """
        random.shuffle(self.all_cards)

    def deal(self, quantity):
        """
        Deals out a specific number of cards from the deck.

        Pops a specific number of Card objects from the list at
        'self.all_cards' within the Deck object and returns them as
        'dealt_cards'. Where 'quantity' = number of cards to return.
        """
        dealt_cards = []
        for _ in range(quantity):
            dealt_cards.append(self.all_cards.pop())
        return dealt_cards
        