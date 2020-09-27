from random import shuffle
import json
from collections import namedtuple

Card = namedtuple('Card',['rank','suit'])
class FrenchDeck:
    ranks = [str(i) for i in range(2,11)] + list("JQKA")
    suits = ['黑桃','梅花','方塊','紅心']
    def __init__(self):
        self.cards = [Card(rank,suit) for rank in FrenchDeck.ranks for suit in FrenchDeck.suits]
    def __len__(self):
        return len(self.cards)
    def __getitem__(self, item):
        return self.cards[item]
    def __setitem__(self, key, value):
        self.cards[key] = value
    def __str__(self):
        return json.dumps(self.cards,ensure_ascii=False)

deck = FrenchDeck()
print(deck)
shuffle(deck)
print(deck)
player1 =deck[:13]
player2 =deck[13:26]
player3 =deck[26:39]
player4 =deck[39:]
print(player1)
print(player2)
print(player3)
print(player4)