import random

def lotto_pull(x):
    lotto_numb = []
    avail_numb =  list(range(1,46))
    for _ in range(x):
        randNumb = avail_numb[random.randint(0, len(avail_numb)-1)]
        avail_numb.remove(randNumb)
        lotto_numb.append(randNumb)
    return lotto_numb

def statistik_lotto(dict_lotto, pulls):
    for number in pulls:
        if number in dict_lotto:
            dict_lotto[number] += 1

dict_lotto = {}
for i in range (1, 46):
    dict_lotto[i] = 0

pulls = 1000

for i in range(pulls):
    statistik_lotto(dict_lotto, lotto_pull(6))

def main():
    print("Statistik:")
    for i in dict_lotto:
        print(f"Die Zahl {i} wurde {dict_lotto[i]} mal gezogen")
        print("")


if __name__ == "__main__":
    main()