import random

def create_deck():
    """Erstellt ein vollständiges Kartendeck mit 52 Karten."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    return deck

def shuffle_deck(deck):
    """Mischt das Kartendeck."""
    random.shuffle(deck)

def deal_card(deck):
    """Gibt die oberste Karte aus dem Deck zurück."""
    return deck.pop()
