#!/usr/local/bin/python3

import random as rd
import sys as sys

class BEGIN:
    def __init__(self, GameBoard, MaxRand: int):
        self._GameBoard = GameBoard
        self._Posx = None
        self._Posy = None
        self.maxRand = MaxRand

    def IAPose(self):
        self._Posx = rd.randrange(0, self.maxRand - 1)
        self._Posy = rd.randrange(0, self.maxRand - 1)
        self._GameBoard[self._Posx][self._Posy] = 1
        print(self._Posx, end=',')
        print(self._Posy)
        sys.stdout.flush()
        return self._GameBoard

    def run(self):
        self.IAPose()
