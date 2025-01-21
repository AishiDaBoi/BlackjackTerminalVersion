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
