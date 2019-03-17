class PlayingCard:
    def __init__(self):
        self.name = None
        # value may be a single integer or if the card is an Ace then it's a list of integers [1,11]
        self.value = None
        self.suit = None

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getSuit(self):
        return self.suit

    def setSuit(self, suit):
        self.suit = suit