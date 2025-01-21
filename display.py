# Farben für das Terminal
CARD_COLORS = {
    'Hearts': '\033[91m',    # Rot
    'Diamonds': '\033[91m',  # Rot
    'Clubs': '\033[97m',     # Weiß
    'Spades': '\033[97m',    # Weiß
    'Trump': '\033[93m'      # Gelb für Trump Cards
}
RESET_COLOR = '\033[0m'  # Zurücksetzen der Farbe
LEVEL_COLORS = {
    1: '\033[92m',  # Grün für Level 1
    2: '\033[93m',  # Gelb für Level 2
    3: '\033[94m'   # Blau für Level 3
}

def display_card(card):
    """Gibt die grafische Darstellung einer einzelnen Karte aus."""
    suit = card['suit']
    value = card['value']

    # Bestimme das Symbol der Karte je nach Farbe
    if suit == 'Hearts':
        suit_symbol = '♥'
        color = '\033[91m'  # Rot
    elif suit == 'Diamonds':
        suit_symbol = '♦'
        color = '\033[91m'  # Rot
    elif suit == 'Clubs':
        suit_symbol = '♣'
        color = '\033[92m'  # Grün
    else:  # Spades
        suit_symbol = '♠'
        color = '\033[94m'  # Blau

    # Handhabe die Karte
    card_display = f"┌─────────────┐\n"
    card_display += f"│ {value:<2}          │\n"  # 2 Zeichen Platz für die Zahl/den Buchstaben
    card_display += f"│             │\n"
    card_display += f"│     {color}{suit_symbol}{RESET_COLOR}      │\n"
    card_display += f"│             │\n"
    card_display += f"└─────────────┘"

    return card_display

def display_hand(hand):
    """Gibt die Karten eines Spielers in einer Hand aus."""
    hand_display = ""
    for card in hand:
        hand_display += display_card(card) + "\n\n"
    return hand_display

