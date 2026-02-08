"""
Program Name: Lab 4 - card dealer
Author: Kaleb Quinn
Purpose: Simulate dealing a hand random cards.
Date: 02/08/2026
"""
import random

def get_num_cards():
    while True:
        user_input = input("How many cards do you want dealt? (1-52): ")

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        num = int(user_input)

        if num < 1 or num > 52:
            print("Number must be between 1 and 52.")
            continue

        return num


def main():
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["c", "h", "s", "d"]

    num_cards = get_num_cards()

    hand = []
    used_cards = set()

    while len(hand) < num_cards:
        value = random.choice(values)
        suit = random.choice(suits)

        card = value + suit

        if card not in used_cards:
            used_cards.add(card)
            hand.append(card)

    print("\nYour hand:")
    for card in hand:
        print(card)

    print("\nTotal cards dealt: " + str(len(hand)))


if __name__ == "__main__":
    main()
