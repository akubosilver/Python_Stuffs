##BlackJack Game in python
import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
         'Seven':7, 'Egiht':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Egiht',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
playing = False
#create cards
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit
#create deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card
#create players hand
class Hand:
    def __init__(self):
        self.cards = [] #start with an empty list
        self.value = 0 #start with zero
        self.aces = 0   #add an attribute to keep track of aces
    
    def add_card(self,card):
        #card passed in
        #from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        #track for ace
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
#chips
class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
#ask player for thier bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips!\nYou have: {chips.total}')
            else:
                break
#Hit
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()            
#hit_or_stand
def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter 'h' or 's' ")
        if x[0].lower() =='h':
            hit(deck,hand)
            playing = False
        elif x[0].lower() == 's':
            print("Player Stands, Dealer's Turn")
            playing = False
        else:
            print("Sorry, please try again with 'h' or 's' only.")
            continue
        break
#showing cards
def show_some(player,dealer):
    #show only one of dealers card
    print("\nDealer's Hand: ")
    print("First card Hidden!")
    print(dealer.cards[1])
    #show all players card
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    #show all dealer's card
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)
    #calculate and display value
    print(f"Value of dealer's hand is: {dealer.value}")
    #show all player's card
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
    #calculate and display value
    print(f"Value of player's hand is: {player.value}")
#win, bust, push
def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS!\nDEALER BUST!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
def push(player,dealer):
    print('Dealer and Player tie!!! PUSH')

###Game proper
while True:
    playing = True
    #opening statement
    print("WELCOME TO BLACKJACK")
    #create & shuffle deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    #set up player's hand
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    #set up dealer's hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    #set up player's chips
    player_chips = Chips()
    #prompt player for thier bet
    take_bet(player_chips)
    #show cards (but keep one of dealer hidden)
    show_some(player_hand,dealer_hand)
    while playing:
        #prompt for player to hit or stand
        hit_or_stand(deck,player_hand)
        #show cards (dealer one hidden)
        show_some(player_hand,dealer_hand)
        #if player's hand exceed 21, run player bust and break
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    #if player hasn't busted, play dealers hand until dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        #show all cards
        show_all(player_hand,dealer_hand)
        #run different winning scenerios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    #inform player of thier remaining chips total
    print(f'\nPlayer total chips are at: {player_chips.total}')
    #ask for replay
    new_game = input("Would you like to play another hand? 'y' or 'n' ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for Playing!")
        break