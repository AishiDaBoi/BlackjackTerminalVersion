import random
from logic import calculate_hand_value, display_hand, check_winner
from deck import create_deck, shuffle_deck, deal_card


def play_game(lives, wins, dealer_wins, level):
    """Hauptspielfunktion für eine Runde."""

    # Initialisieren der Hände
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print(f"\n--- Runde {wins + dealer_wins + 1} ---")
    print(f"Level {level}")
    print(f"Du hast {lives} Leben.")
    print(f"Deine Karten:")
    print(display_hand(player_hand))

    if level > 1:
        # Trump Card Logic (im Level 2 und 3)
        trump_card = random.choice(["Reversal", "DoubleDown", "Swap"])
        use_trump = input(f"Möchtest du die Trump Card {trump_card} verwenden? (Ja/Nein): ").strip().lower()
        if use_trump == "ja":
            print(f"Du hast die Trump Card '{trump_card}' verwendet!")
            # Implementiere die spezifischen Effekte der Trump Cards hier

    print("Was möchtest du tun? (Hit/Stand):")
    action = input().strip().lower()

    # Spieleraktionen
    if action == "hit":
        player_hand.append(deal_card(deck))
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    print("\nDer Dealer zieht seine Karten:")
    print(f"Dealer's Karten:\n{display_hand(dealer_hand)}")

    winner, player_wins = check_winner(player_hand, dealer_hand)

    if player_wins:
        print("Du hast gewonnen diese Runde!")
        wins += 1
    else:
        print("Du hast verloren diese Runde.")
        lives -= 1  # Leben nur um 1 verringern, wenn der Spieler verloren hat

    return lives, wins, dealer_wins


def main():
    lives = 5  # Setze die Start-Leben
    wins = 0
    dealer_wins = 0
    level = 1  # Level 1 beginnt

    while lives > 0:
        lives, wins, dealer_wins = play_game(lives, wins, dealer_wins, level)

        if wins == 3 and level == 1:
            level = 2  # Steige zu Level 2 auf
            print("\nDu hast 3 Runden gewonnen und bist nun auf Level 2!")
        elif wins == 3 and level == 2:
            level = 3  # Steige zu Level 3 auf
            print("\nDu hast 3 Runden gewonnen und bist nun auf Level 3!")
        elif dealer_wins == 5:
            print("\nDer Dealer hat 5 Runden gewonnen! Spiel vorbei!")
            break
        elif wins == 5:
            print("\nDu hast 5 Runden gewonnen! Herzlichen Glückwunsch!")
            break

        if level == 3 and wins == 5:
            print("\nDu hast das Spiel gewonnen!")
            break
        elif lives == 0:
            print("\nDu hast keine Leben mehr. Spiel vorbei!")
            break


if __name__ == "__main__":
    main()
