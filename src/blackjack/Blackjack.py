from PlayingCard import PlayingCard
from DeckOfCards import DeckOfCards

class Blackjack:
    def __init__(self):
        self.dealers_hand = []
        self.players_hand = []
        self.deck = DeckOfCards()
        self.last_ace_choice = None
        print('Welcome to the BlackJack game')

    def hit(self, player_type):
        # Dealer only hits if their current hand is worth 13 or less
        if (player_type == 'dealer') and self.dealerCanHit() :
            self.dealers_hand.append(self.deck.getRandomCard())
        elif (player_type == 'player'):
            self.players_hand.append(self.deck.getRandomCard())
            if len(self.players_hand) > 1:
                self.printHand(player_type)

    def dealerCanHit(self):
        if self.getDealerHandValue() < 14:
            return True
        else:
            return False

    def deal(self):
        self.hit('player')
        self.hit('player')
        self.hit('dealer')
        self.hit('dealer')
        self.printHand('dealer', True)

    def printHand(self, player_type, firstCardOnly=False):
        if firstCardOnly and (player_type == 'dealer'):
            print('The dealer is showing a ' + self.dealers_hand[0].getName() + ' of ' + self.dealers_hand[0].getSuit())
        elif not firstCardOnly and (player_type == 'player'):
            print('You have the following cards: ')
            for card in self.players_hand:
                print(card.getName() + ' of ' + card.getSuit())

    def checkForBust(self, player_type):
        if player_type == 'player':
            if self.getPlayerHandValue(True) > 21:
                return True
            else:
                return False
        else:
            if self.getDealerHandValue() > 21:
                return True
            else:
                return False

    def whoIsWinner(self):
        dealer_val = self.getDealerHandValue()
        player_val = self.getPlayerHandValue(False)
        if dealer_val > 21 and player_val < 21:
            print('Dealer busted, Player wins!')
        elif dealer_val < 21 and player_val > 21:
            print('Player busted, Dealer wins!')
        elif dealer_val > player_val:
            print('Dealer won with a hand value of ' + str(dealer_val) + '!')
        elif dealer_val < player_val:
            print('Player won with a hand value of ' + str(player_val) + '!')
        elif dealer_val == player_val:
            print('Player and dealer have same hand value, push!')
        else:
            raise Exception('Software cannot figure out who won, it must have a bug somewhere')

    def getDealerHandValue(self):
        total_val = 0
        ace_in_hand = False
        for card in self.dealers_hand:
            currVal = card.getValue()
            # if card is an Ace, choose 11 as value for now
            if type(currVal) == list:
                ace_in_hand = True
                currVal = 11
            total_val += currVal
        # if dealer has an Ace and is going to bust then choose Ace value to be 1 instead of 11
        if ace_in_hand and total_val > 21:
            total_val -= 10
        return total_val

    def getPlayerHandValue(self,hit):
        total_val = 0
        for card in self.players_hand:
            currVal = card.getValue()
            # if card is an Ace, ask the user if they'd like it to take on the value 1 or 11
            if type(currVal) == list:
                if hit:
                    currVal = int(input('An Ace is in your hand, would you like it to have the value 1 or 11?'))
                    self.last_ace_choice = currVal
                    if currVal not in [1,11]:
                        raise Exception('Your Ace must have a value of 1 or 11 but you chose a different value, game over!')
                else:
                    currVal = self.last_ace_choice
            total_val += currVal
        return total_val

    def resetGame(self):
        self.dealers_hand = []
        self.players_hand = []
        self.deck.resetCards()
        self.last_ace_choice = None


def main():
    theGame = Blackjack()
    playAgain = True
    player_busted = False
    while (playAgain):
        theGame.deal()
        stillHitting = True
        neverHit = True
        while (stillHitting):
            hitAnswer = input('Would you like to hit? y or n?')
            if hitAnswer == 'y':
                neverHit = False
                theGame.hit('player')
                if theGame.checkForBust('player'):
                    theGame.whoIsWinner()
                    player_busted = True
                    break
            elif hitAnswer == 'n':
                stillHitting = False
            else:
                raise Exception('You must type "y" or "n" but you typed something different, game over!')
        if neverHit:
            theGame.checkForBust('player')
        if not player_busted:
            while theGame.dealerCanHit():
                theGame.hit('dealer')
            theGame.whoIsWinner()
        playAgainAnswer = input('Would you like to play again?, y or n?')
        if playAgainAnswer == 'n':
            playAgain = False
        elif playAgainAnswer == 'y':
            theGame.resetGame()
        elif playAgainAnswer != 'y':
            raise Exception('You must type "y" or "n" but you typed something different, not playing again then!')

if __name__ == '__main__':
    main()
