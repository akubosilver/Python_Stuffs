#War_Game in python
#global variables and and necessary libraries
import random
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
         'Seven':7, 'Egiht':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Egiht',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#card ---> suits,rank,value
class Card:
    """
    Each card has a suit,rank and a value
    This generates each if the unique card for the players
    """
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
#deck --->generates the 52 deck of cards
class Deck:
    """
    instantiate a new deck of 52 cards and hold as a list of cards object
    shuffle a deck through random method call
    Deal cards from the deck object and pop method from card list
    """
    def __init__(self):
    #create the deck and hold in the list
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
    #shuffle all created cards
        random.shuffle(self.all_cards)

    def deal_one(self):
    #deal a card by popping it
        return self.all_cards.pop()
#player
class Player:
    """
    Creates a new player with all needed card and
    methods for adding and removing card during the game
    """
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
#game_logic
#game setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()
#split deck of shuffled card and deal half to each player
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
#start game
game_on = True
#round of game at start
round_num = 0
#game_loop
while game_on:
    round_num += 1
    print(f'Round {round_num}')
    #check for win
    if len(player_one.all_cards) == 0:
        print('Player One is out of cards!\nplayer Two wins!!!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
            print('Player Two is out of cards!\nplayer One wins!!!')
            game_on = False
            break
    #start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    #at war
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!!!")
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("Player Two Wins!!!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("Player One Wins!!!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())