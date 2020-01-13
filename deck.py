import random

MIN_CARD_RANGE = 1
MAX_CARD_RANGE = 10
CARDS_RANGE = range(MIN_CARD_RANGE, MAX_CARD_RANGE + 1)
COLORS = {"red", "blue", "green", "yellow"}
CARD_SEPARATOR = "\n"


class Card:
    def __init__(self, number, ctype):
        self.number = number
        self.type = ctype
        self.assert_input()

    def assert_input(self):
        assert (self.number in CARDS_RANGE)
        assert (self.type in COLORS)

    def __str__(self):
        return f"Number: {self.number}, Color: {self.type}"


class Deck:
    def __init__(self):
        self.deck = [Card(number, ctype) for number in CARDS_RANGE
                     for ctype in COLORS]

    def assert_input(self):
        assert (len(self.deck) == len(CARDS_RANGE) * len(COLORS))

    def __str__(self):
        return CARD_SEPARATOR.join(str(card) for card in self.deck)

    def __bool__(self):
        return len(self.deck) > 0

    def __getitem__(self, item):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)


if __name__ == "__main__":
    my_deck = Deck()
    my_deck.shuffle()
    
    for card in my_deck:
        print(card)

    if my_deck:
        print("Something is wrong")
    else:
        print("The deck is empty.")
