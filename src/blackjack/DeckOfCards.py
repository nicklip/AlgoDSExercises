from random import randrange
from PlayingCard import PlayingCard

class DeckOfCards:
    def __init__(self):
        self.cards = []
        self.resetCards()

    def resetCards(self):
        # loop through each suit
        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        self.cards = []
        for suit in suits:
            # loop through each card in suit
            for i in range(2,15):
                currCard = PlayingCard()
                if (i < 11):
                    currCard.setName(str(i))
                    currCard.setValue(i)
                elif (i < 14):
                    currCard.setValue(10)
                    if (i == 11):
                        currCard.setName('Jack')
                    elif (i == 12):
                        currCard.setName('Queen')
                    elif (i == 13):
                        currCard.setName('King')
                else:
                    currCard.setName('Ace')
                    currCard.setValue([1,11])
                currCard.setSuit(suit)
                self.cards.append(currCard)


    def getNumCardsLeft(self):
        return len(self.cards)

    def getRandomCard(self):
        # get index of random card from the deck
        random_index = randrange(len(self.cards))
        # get card corresponding the random index
        random_card = self.cards[random_index]
        # remove the random card from the deck
        del self.cards[random_index]
        return random_card


def main():
    # testing DeckOfCards and PlayingCard classes
    aDeck = DeckOfCards()
    aCard = aDeck.getRandomCard()
    print('The card you picked is a ' + aCard.getName() + ' of ' + aCard.getSuit())
    print('You now have ' + str(aDeck.getNumCardsLeft()) + ' cards left')
    print('Resetting card deck...')
    aDeck.resetCards()
    print('You now have ' + str(aDeck.getNumCardsLeft()) + ' cards again')


if __name__ == '__main__':
    main()