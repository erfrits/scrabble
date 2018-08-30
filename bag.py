import json
import random as rnd
from math import floor


class Bag:

    _letters = []

    def __init__(self):
        with open(".\\resource\\letterDist") as f:
            lDict = json.load(f)
        for l in lDict:
            s = l * lDict[l]
            self._letters += list(s)
        for i in range(floor((rnd.random() + 1) * 25)):
            rnd.shuffle(self._letters)
        # print(self.letters)

    def draw(self, n):
        __lDrawn = []
        for i in range(n):
            rnd.shuffle(self._letters)
            __lDrawn += self._letters.pop(floor(rnd.random() * len(self._letters)))
        return __lDrawn


if __name__ == '__main__':
    bag: Bag = Bag()
    print(bag.draw(5))
