def calculate_hand_value(hand):
    """Berechnet den Wert der Hand (Spieler oder Dealer)."""
    value = 0
    aces = 0  # Zählt die Asse

    for card in hand:
        if card['value'] in ['J', 'Q', 'K']:
            value += 10
        elif card['value'] == 'A':
            aces += 1
            value += 11
        else:
            value += int(card['value'])

    # Berücksichtige Asse als 1, wenn der Wert über 21 geht
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


def display_hand(hand):
    """Zeigt die Karten eines Spielers als rechteckige Karten im Terminal an."""
    symbol_dict = {
        'Hearts': '♥',
        'Diamonds': '♦',
        'Clubs': '♣',
        'Spades': '♠'
    }

    lines = [''] * 7  # Karten bestehen jetzt aus 7 Zeilen, damit sie höher sind
    for card in hand:
        symbol = symbol_dict[card['suit']]  # Holen des Symbols aus dem Dictionary
        lines[0] += " ┌─────────────┐  "
        lines[1] += f" |{card['value']: <2}           |  "  # Kartenwert, z.B. 'K', '10'
        lines[2] += " |             |  "
        lines[3] += f" |     {symbol}       |  "  # Das Symbol der Karte, z.B. ♥, ♠, ♦, ♣
        lines[4] += " |             |  "
        lines[5] += " |             |  "
        lines[6] += " └─────────────┘  "

    return "\n".join(lines)


def check_winner(player_hand, dealer_hand):
    """Überprüft, wer in der Runde gewonnen hat."""
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21:  # Spieler hat überzogen
        return "dealer", False
    elif dealer_value > 21:  # Dealer hat überzogen
        return "player", True
    elif player_value > dealer_value:  # Spieler hat mehr
        return "player", True
    elif player_value < dealer_value:  # Dealer hat mehr
        return "dealer", False
    else:  # Unentschieden
        return "tie", None
