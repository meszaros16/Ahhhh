import random


szam = random.randint(1, 5)

szam2 = int(input("Adj meg egy véletlen számot"))


if szam2 > szam:
    print("A szám nagyobb")


if szam2 < szam:
    print("A szám kisebb")


if szam2 == szam:
    print("talált")

