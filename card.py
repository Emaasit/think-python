"""This is Chapter 18: Inheritance

Learning Python programming using the book titled

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2017 Daniel Emaasit

License: http://creativecommons.org/licenses/by/4.0/
"""
from random import shuffle

class Card:
    """Represents the cards in deck
    
    Attributes
    ----------
    suits : int
    ranks : int
    """
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit = 0, rank = 2):
        """Initialize a Card object
        """
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return "%s of %s" % (Card.suit_names[self.suit], Card.rank_names[self.rank])
    
    def __lt__(self, other):
        # using tuple comparison
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    
class Deck:
    """Represents a deck of 52 cards"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)    
    
    def remove_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
        
    def shuffle_deck(self):
        shuffle(self.cards)
        
class Hand(Deck):
    """Represents a Hand which inherits from Deck class"""
    def __init__(self, label = ""):
        self.cards = []
        self.label = label