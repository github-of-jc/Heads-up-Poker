"""
Head-up no limit hold'em Poker player by Jiayi Chen

"""
import numpy as np

import random

class Player():
    """Player class"""

    def __init__(self, name):
        self.button = False
        self.name = name
        self.wealth = 1000
        self.bet_size = 0
        self.money_in = 0

    def call(self, amount):
        self.bet_size = amount
        print("My name is", self.name)

    def bet(self, amount):
        self.bet_size = amount
        print(self.name, "is betting", amount)

    def fold(self):
        self.bet_size = 0
        print(self.name, "is folding.")
    
    def getInfo(self):
        print(self.name, self.button, self.amount)
        
class Card():
    """Card class that generates a random list of cards to be dealt out at each game"""
    # a list of card
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def print_card(self):
        print(self.rank, self.suit)
        
class Deck():
    """class that creates card and shuffle them, then deals them"""
    
    def __init__(self):
        #13 ranks
        #4 suits
        rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suit = ['Club', 'Diamond','Heart','Spade']
        self.deck = []
        for x in rank:
            #print(x)
            for y in suit:
                #print(y)
                card = Card(x, y)
                self.deck.append(card)
        
    def print_deck(self):
        for x in self.deck:
            x.print_card()
            
    def shuffle_deck(self):
        shuffle(self.deck)
    
    def pop(self):
        popped_card = self.deck.pop()
        popped_card.print_card()
        
        
        
class Game():
    """Class to play with players"""
    #class variables
    
    
    def __init__(self):
        print("inited play")
        self.small_blind = 10
        self.big_blind = 20
        self.pool = 0
        self.deck = Deck()
        self.deck.shuffle_deck()
        print("shuffled")
        #self.deck.print_deck()
        
    def deal(self):
        print("calling deal deck")
        """pops the first card from the random deck"""
        self.deck.pop() 
    
    
        
    


button = 1
small_blind = 10
big_blind = 20

Drago = Player("Drago")
Daenerys = Player("Daenerys")
Drago.getInfo()
Daenerys.getInfo()

p = Game()
p.deal()

