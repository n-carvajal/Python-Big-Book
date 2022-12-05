"""Player Class"""


class Player:
    """
    Player class and its associated attributes and methods.
    """

    def __init__(self, name, bankroll):
        """
        Defines Player object attributes upon instantiation.
        """
        self.name = name
        self.bankroll = bankroll
        self.hand = []

    def __str__(self):
        """
        Returns print string for Player object
        """
        return f"{self.name} has a bankroll of ${round(self.bankroll)}"

    def gather_hand(self, cards):
        """
        Adds dealt cards to Player object's 'self.hand' attribute.

        Appends the Card objects in 'cards' to 'self.hand'. Where
        'cards' = list of Card objects.
        """
        for card in cards:
            self.hand.append(card)

    def show_hand(self, show_all=True):
        """
        Displays an ASCII version of the Card objects within the
        'self.hand' attribute of the Player object.

        It does so by looping through the number of cards in 'self.hand'
        and concatenating a series of formatted strings to generate an
        ASCII representation of the list at 'self.hand'.  Where
        'show_all=True' displays the first card at 'self.hand' as being
        face up and 'show_all=False' displays the first card at
        'self.hand' as being face down. Returns ASCII print string.
        """
        rows = ["", "", "", "", ""]
        if show_all:
            for card in self.hand:
                if card.rank != "10":
                    rows[0] += "  _____  "
                    rows[1] += f" |{card.rank}____| "
                    rows[2] += f" |__{card.suit}__| "
                    rows[3] += f" |____{card.rank}| "
                else:
                    rows[0] += "  _____  "
                    rows[1] += f" |{card.rank}___| "
                    rows[2] += f" |__{card.suit}__| "
                    rows[3] += f" |___{card.rank}| "
            for row in rows:
                print(row)
        else:
            for i, card in enumerate(self.hand):
                if i == 0:
                    rows[0] += "  _____  "
                    rows[1] += " |_____| "
                    rows[2] += " |_____| "
                    rows[3] += " |_____| "
                else:
                    if card.rank != "10":
                        rows[0] += "  _____  "
                        rows[1] += f" |{card.rank}____| "
                        rows[2] += f" |__{card.suit}__| "
                        rows[3] += f" |____{card.rank}| "
                    else:
                        rows[0] += "  _____  "
                        rows[1] += f" |{card.rank}___| "
                        rows[2] += f" |__{card.suit}__| "
                        rows[3] += f" |___{card.rank}| "
            for row in rows:
                print(row)

    def score_hand(self):
        """
        Returns the score of a players hand.

        Creates 'score' and sets it equal to zero. Then it loops through
        the Card objects within 'self.hand' of the Player object and for
        every card it adds its 'card.value' to 'score'. When looping
        finished it returns 'score'.
        """
        score = 0
        for card in self.hand:
            score += card.value
        return score

    def bet(self, amount):
        """
        Removes bet amount from the player's total.
        """
        self.bankroll -= amount
        return amount

    def collect_winnings(self, amount):
        """
        Adds winnings to player's total.
        """
        self.bankroll += amount
