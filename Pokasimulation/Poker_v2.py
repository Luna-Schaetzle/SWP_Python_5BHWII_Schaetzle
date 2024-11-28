import random
from collections import Counter

# Create a deck with all cards
def reset_deck():
    # Define suits and card types
    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    card_types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [(suit, card_type) for suit in suits for card_type in card_types]

# Function to draw a card and remove it from the deck
def draw_card(deck):
    drawn_card = random.choice(deck)
    deck.remove(drawn_card)
    return drawn_card

# Function to draw a hand
def draw_hand(deck, hand_size):
    return [draw_card(deck) for _ in range(hand_size)]

# Function to assign the correct value to card types
def set_rank(card):
    rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'Jack': 9, 'Queen': 10, 'King': 11, 'Ace': 12}
    return rank_order[card]

# Function to sort the hand by ranks
def set_order(hand):
    return sorted(hand, key=lambda card: set_rank(card[1]))

# Function to check for a Royal Flush
def royal_flush(hand):
    royal_flush_order = ['10', 'Jack', 'Queen', 'King', 'Ace']
    suits_in_hand = [card[0] for card in hand]
    cards_in_hand = [card[1] for card in hand]
    return len(set(suits_in_hand)) == 1 and all(card_type in cards_in_hand for card_type in royal_flush_order)

# Function to determine poker combinations
def determine_combination(hand, hand_size):
    suits_in_hand = [card[0] for card in hand]
    cards_in_hand = [card[1] for card in hand]
    cards_counter = Counter(cards_in_hand)
    
    ordered_hand = set_order(hand)
    ordered_values = [set_rank(card[1]) for card in ordered_hand]
    
    # Royal Flush
    if royal_flush(hand):
        return "Royal Flush"

    # Straight Flush
    if len(set(suits_in_hand)) == 1 and ordered_values == list(range(ordered_values[0], ordered_values[0] + hand_size)):
        return "Straight Flush"
    
    # Four of a Kind
    if 4 in cards_counter.values():
        return "Four of a Kind"

    # Full House
    if 2 in cards_counter.values() and 3 in cards_counter.values():
        return "Full House"

    # Flush
    if len(set(suits_in_hand)) == 1:
        return "Flush"

    # Straight
    if ordered_values == list(range(ordered_values[0], ordered_values[0] + hand_size)):
        return "Straight"

    # Three of a Kind
    if 3 in cards_counter.values():
        return "Three of a Kind"

    # Two Pair
    if list(cards_counter.values()).count(2) == 2:
        return "Two Pair"

    # One Pair
    if 2 in cards_counter.values():
        return "One Pair"

    # High Card
    return "High Card"

# Collect statistics
def collect_statistics(draws, hand_size, combinations_counter):
    for _ in range(draws):
        deck = reset_deck()
        hand = draw_hand(deck, hand_size)
        combination = determine_combination(hand, hand_size)
        combinations_counter[combination] += 1

    # Output the results
    for combination, count in combinations_counter.items():
        print(f"{combination}: {count} ({count/draws*100:.9f}%)")


def main():
    # We create a dictionary to store how often each possibility has occurred
# you could use defaultdict(int) instead it would be a smoother way to do it
    combinations_counter = { 
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two Pair": 0,
    "One Pair": 0,
    "High Card": 0
    }
    try:
        draws = int(input("How many draws would you like to simulate? "))
        hand_size = int(input("How many cards should be in a hand? (Normaly 5)"))
        collect_statistics(draws, hand_size, combinations_counter)
        print(f"{draws} draws simulated with {hand_size} cards in a hand.")
    except ValueError:
        print("Please enter a valid number.")


# Main function to run the test
if __name__ == "__main__":
    main()
