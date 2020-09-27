from random import shuffle

class FrenchDeck:
    ranks = [str(i) for i in range(2,11)] + list('JQKA')
    suits = ['黑桃','梅花','方塊','紅心']
    def __init__(self):
        self.cards = [(rank,suit) for rank in FrenchDeck.ranks for suit in FrenchDeck.suits]
    def __len__(self):
        return len(self.cards)
    def __getitem__(self, item):
        return self.cards[item]
    def __setitem__(self, key, value):
        self.cards[key]=value
deck = FrenchDeck()
print(deck.__dict__)
print(deck[0])
shuffle(deck)
print(deck[:13])
print(deck[13:26])
print(deck[26:39])
print(deck[39:])
