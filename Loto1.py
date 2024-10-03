import random


def lotto_ziehung(x):
    lotto_zahlen = []
    available_zahlen = list(range(1, 46)) 
    for _ in range(x):
        randomZahl = available_zahlen[random.randint(0, len(available_zahlen)-1)] 
        available_zahlen.remove(randomZahl)   
        lotto_zahlen.append(randomZahl)       

    return lotto_zahlen

def statisik_lotto(dict_lotto, ziehungen):
    for zahl in ziehungen:
        if zahl in dict_lotto:
            dict_lotto[zahl] += 1

dict_lotto = {}
for i in range(1, 46):
    dict_lotto[i] = 0


ziehungen = 1000

for i in range(1, ziehungen):
    statisik_lotto(dict_lotto, lotto_ziehung(6))


print("Statistik:")
for i in dict_lotto:
    print(f"Die Zahl {i} wurde {dict_lotto[i]} mal gezogen")
    print("")