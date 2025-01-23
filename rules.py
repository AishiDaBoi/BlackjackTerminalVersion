from deck import shuffle_deck


def check_level_up(wins, level, lives, deck):
    """Überprüfe, ob der Spieler ins nächste Level aufsteigt."""
    if level == 1 and wins == 3:
        print("Du hast 3 Mal gewonnen. Du steigst ins Level 2 auf!")
        level += 1
        wins = 0
        shuffle_deck(deck)  # Deck für das nächste Level neu mischen
    elif level == 2 and wins == 3:
        print("Du hast 3 Mal gewonnen. Du steigst ins Level 3 auf!")
        level += 1
        wins = 0
        shuffle_deck(deck)
    return level, wins

def check_dealer_loss(dealer_wins):
    """Überprüfe, ob der Dealer das Spiel gewonnen hat (5 Siege)."""
    if dealer_wins == 5:
        return True
    return False
