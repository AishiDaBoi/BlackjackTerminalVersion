import random

# Importiere die Funktionen und Konstanten aus der Karte
from card_display import display_card, display_hand, create_deck, shuffle_deck, deal_card


def calculate_hand_value(hand):
    """Berechnet den Wert einer Hand im Blackjack."""
    value = 0
    ace_count = 0

    for card in hand:
        if card['value'] in ['J', 'Q', 'K']:
            value += 10
        elif card['value'] == 'A':
            value += 11
            ace_count += 1
        else:
            value += int(card['value'])

    # Aces als 1 zählen, wenn der Wert über 21 geht
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1

    return value


def print_game_state(player_hand, dealer_hand, reveal_dealer_card=False):
    """Zeigt den aktuellen Stand des Spiels an."""
    print("Spielstand:")
    print(f"{display_hand(player_hand)}")
    print(f"Wert der Spieler Hand: {calculate_hand_value(player_hand)}")

    if reveal_dealer_card:
        print("Dealer Hand:")
        print(f"{display_hand(dealer_hand)}")
        print("Dealer Hand:")
        print(f"{calculate_hand_value(dealer_hand)}")
    else:
        # Zeige nur die sichtbare Karte des Dealers
        print("Dealer Hand:")
        print(f"{display_card(dealer_hand[0])}  [verdeckt]")

    print("\n")


def play_blackjack():
    """Startet das Blackjack-Spiel."""
    # Initialisiere das Deck und mische es
    deck = create_deck()
    shuffle_deck(deck)

    # Teile die Karten aus
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Zeige den Anfangszustand
    print_game_state(player_hand, dealer_hand, reveal_dealer_card=False)

    # Spielerzug
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value > 21:
            print("Du hast überkauft (Busted)! Dealer gewinnt.")
            return

        action = input("Möchtest du 'HIT' (ziehen) oder 'STAND' (passen)? ").lower()
        if action == 'hit':
            player_hand.append(deal_card(deck))
            print_game_state(player_hand, dealer_hand, reveal_dealer_card=False)
        elif action == 'stand':
            break
        else:
            print("Ungültige Eingabe. Bitte 'HIT' oder 'STAND' eingeben.")

    # Dealerzug
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        print_game_state(player_hand, dealer_hand, reveal_dealer_card=True)

    # Berechne die Ergebnisse
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("Dealer hat überkauft! Du gewinnst!")
    elif player_value > dealer_value:
        print("Du gewinnst!")
    elif player_value < dealer_value:
        print("Dealer gewinnt!")
    else:
        print("Unentschieden!")


if __name__ == '__main__':
    print("Willkommen bei Blackjack!")
    play_blackjack()
