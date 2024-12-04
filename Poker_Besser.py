import random
from collections import Counter
import unittest


def erstelle_deck():
    farben = ['Kreuz', 'Pik', 'Herz', 'Karo']
    zahlen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [f"{zahl} {farbe}" for zahl in zahlen for farbe in farben]


def gezogene_Hand(deck, karten=5):
    return random.sample(deck, karten)


def karten_wert(karte):
    zahl = karte.split()[0]
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[zahl]


def hand_lesen(hand):
    values = sorted([karten_wert(karte) for karte in hand])  
    farben = [karte.split()[1] for karte in hand]            
    value_counts = Counter(values)                          

    if len(set(farben)) == 1 and values == list(range(values[0], values[0] + 5)):
        return "Royal Flush" if values[0] == 10 else "Straight Flush"
    elif 4 in value_counts.values():
        return "Four of a Kind"
    elif 3 in value_counts.values() and 2 in value_counts.values():
        return "Full House"
    elif len(set(farben)) == 1:
        return "Flush"
    elif values == list(range(values[0], values[0] + 5)):
        return "Straight"
    elif 3 in value_counts.values():
        return "Three of a Kind"
    elif list(value_counts.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in value_counts.values():
        return "One Pair"
    else:
        return "High Card"


def simulation_poker(versuche, deck):
    hand_counts = Counter()
    for _ in range(versuche):
        hand = gezogene_Hand(deck)
        hand_art = hand_lesen(hand)
        hand_counts[hand_art] += 1
    return hand_counts


def main():
    versuche = int(input("Wie viele Pokerhände sollen simuliert werden? "))
    deck = erstelle_deck()
    hand_counts = simulation_poker(versuche, deck)

    print("\nSimulierte Pokerhände:")
    for hand_art, count in hand_counts.items():
        prozente = (count / versuche) * 100
        print(f"{hand_art}: {prozente:.2f}%")


if __name__ == "__main__":
    main()

# Unit Tests
class TestPokerSimulation(unittest.TestCase):

    def test_karten_wert(self):
        self.assertEqual(karten_wert("2 Kreuz"), 2)
        self.assertEqual(karten_wert("10 Pik"), 10)
        self.assertEqual(karten_wert("J Herz"), 11)
        self.assertEqual(karten_wert("Q Karo"), 12)
        self.assertEqual(karten_wert("K Kreuz"), 13)
        self.assertEqual(karten_wert("A Pik"), 14)

    def test_hand_lesen(self):
        deck = erstelle_deck()
        self.assertEqual(hand_lesen(["10 Kreuz", "J Kreuz", "Q Kreuz", "K Kreuz", "A Kreuz"]), "Royal Flush")
        self.assertEqual(hand_lesen(["2 Pik", "3 Pik", "4 Pik", "5 Pik", "6 Pik"]), "Straight Flush")
        self.assertEqual(hand_lesen(["3 Karo", "3 Kreuz", "3 Herz", "3 Pik", "8 Karo"]), "Four of a Kind")
        self.assertEqual(hand_lesen(["9 Herz", "9 Karo", "9 Pik", "5 Kreuz", "5 Pik"]), "Full House")
        self.assertEqual(hand_lesen(["2 Herz", "4 Herz", "6 Herz", "8 Herz", "10 Herz"]), "Flush")
        self.assertEqual(hand_lesen(["7 Karo", "8 Karo", "9 Karo", "10 Karo", "J Karo"]), "Straight")
        self.assertEqual(hand_lesen(["5 Pik", "5 Herz", "5 Kreuz", "2 Karo", "8 Herz"]), "Three of a Kind")
        self.assertEqual(hand_lesen(["4 Herz", "4 Karo", "7 Pik", "7 Karo", "Q Kreuz"]), "Two Pair")
        self.assertEqual(hand_lesen(["9 Herz", "9 Karo", "2 Kreuz", "5 Pik", "6 Karo"]), "One Pair")
        self.assertEqual(hand_lesen(["2 Pik", "5 Herz", "8 Karo", "J Kreuz", "K Herz"]), "High Card")

    def test_gezogene_hand(self):
        deck = erstelle_deck()
        hand = gezogene_Hand(deck)
        self.assertEqual(len(hand), 5)
        self.assertTrue(all(karte in deck for karte in hand))


if __name__ == "__main__":
    unittest.main()
