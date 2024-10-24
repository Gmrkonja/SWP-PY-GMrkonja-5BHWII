import random
from collections import Counter


Farbe = ['Kreuz', 'Pik', 'Herz', 'Karo']  
Zahl = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  


deck = [zahl + " " + farbe for zahl in Zahl for farbe in Farbe]


def gezogene_Hand():
    return random.sample(deck, 5)


def Karten_Wert(karte):
    zahl = karte.split()[0]
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[zahl]


def Hand_lesen(hand):
    values = sorted([Karten_Wert(karte) for karte in hand])  
    Farbe = [karte.split()[1] for karte in hand]  
    value_counts = Counter(values)  
    
    # Prüfen auf Paar, Drilling, Vierling usw.
    if len(set(Farbe)) == 1 and values == list(range(values[0], values[0] + 5)):  # Straight Flush
        return "Royal Flush" if values[0] == 10 else "Straight Flush"
    elif 4 in value_counts.values():
        return "Four of a Kind"
    elif 3 in value_counts.values() and 2 in value_counts.values():
        return "Full House"
    elif len(set(Farbe)) == 1:
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


def Simulation_Poker(versuche=100000):
    hand_counts = Counter()
    for _ in range(versuche): 
        hand = gezogene_Hand()
        Hand_Art = Hand_lesen(hand)
        hand_counts[Hand_Art] += 1
    return hand_counts

# Simulation starten
hand_counts = Simulation_Poker()


insgesamte_Haende = 100000
print("Simulierte Pokerhände:")
for Hand_Art, count in hand_counts.items():
    prozente = (count / insgesamte_Haende) * 100
    print(Hand_Art + ": " + str(round(prozente, 2)) + "%")
