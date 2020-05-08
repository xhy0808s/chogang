# Number memorization Game.py

import os
from random import *

cards = []

def setup():
    for i in range(1, 10):
        cards.append(i)
        cards.append(i)

    shuffle(cards)

setup()
print(cards)

count = len(cards)

while True:
    a = int(input("숫자를 입력하세요 : "))
    b = int(input("숫자를 입력하세요 : "))

    os.system("cls")

    if (cards[a] == 0) or (cards[b] == 0):
        print("이미 맞추신 카드입니다.")
    elif cards[a] == cards[b]:
        print("맞았습니다")
        cards[a], cards[b] = 0, 0
        count = count - 2
        print(count, " 개 남았습니다")
    else:
        print("땡")
        print("cards[{0}] = {1}, cards[{2}] = {3}".format(a, cards[a], b, cards[b]))