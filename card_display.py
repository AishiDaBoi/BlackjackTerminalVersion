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

# Farben und Symbole für die Karten
CARD_COLORS = {
    'Hearts': '\033[91m',    # Rot
    'Diamonds': '\033[91m',  # Rot
    'Clubs': '\033[97m',     # Weiß
    'Spades': '\033[97m',    # Weiß
}
RESET_COLOR = '\033[0m'  # Zurücksetzen der Farbe

def display_card(card):
    """Stellt eine Karte grafisch und farbig dar."""
    suit_symbols = {
        'Hearts': '♥',
        'Diamonds': '♦',
        'Clubs': '♣',
        'Spades': '♠',
    }
    suit = suit_symbols[card['suit']]
    value = card['value']
    color = CARD_COLORS[card['suit']]

    # Grafische Darstellung der Karte
    card_art = f"""
    {color}┌─────────┐{RESET_COLOR}
    {color}│ {value:<2}      │{RESET_COLOR}
    {color}│         │{RESET_COLOR}
    {color}│    {suit}    │{RESET_COLOR}
    {color}│         │{RESET_COLOR}
    {color}│      {value:>2} │{RESET_COLOR}
    {color}└─────────┘{RESET_COLOR}
    """
    return card_art

def display_hand(cards):
    """Zeigt eine Hand (mehrere Karten) nebeneinander."""
    card_lines = [""] * 6
    for card in cards:
        suit_symbols = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠',
        }
        suit = suit_symbols[card['suit']]
        value = card['value']
        color = CARD_COLORS[card['suit']]

        card_art = [
            f"{color}┌─────────┐{RESET_COLOR}",
            f"{color}│ {value:<2}      │{RESET_COLOR}",
            f"{color}│         │{RESET_COLOR}",
            f"{color}│    {suit}    │{RESET_COLOR}",
            f"{color}│         │{RESET_COLOR}",
            f"{color}└─────────┘{RESET_COLOR}"
        ]

        for i in range(6):
            card_lines[i] += card_art[i] + "  "

    return "\n".join(card_lines)
