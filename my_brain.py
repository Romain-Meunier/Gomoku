#!/usr/local/bin/python3

import sys as sys

class BRAIN:
    def __init__(self, GameBoard, maxsize):
        self._GameBoard = GameBoard
        self._maxsize = maxsize
        self.PosX = 0
        self.PosY = 0
        self.temp = 1

    def print_Tab(self, size: int):
        i = 0
        for line in range(size):
            i = i + 1
            print(self._GameBoard[line])

    def BrainMove(self):
        print("Etape 1")

        for self.PosX in range(len(self._GameBoard)):
            for self.PosY in range(len(self._GameBoard[self.PosX])):
                temp = self.PosY + 4
                print("Etape 2")
                if self._GameBoard[self.PosX][self.PosY] == 1 and self._GameBoard[self.PosX][self.PosY + 4] == 1:
                    print("Etape 3")
                    self.PosY = self.temp
                    while self.temp != self.PosY + 4:
                        print("La position de temp :")
                        print(temp)
                        print("la position de PosY :")
                        print(self.PosY)
                        print("Etape 4")
                        if self._GameBoard[self.PosX][self.temp] == 0:
                            print("Etape 5)")
                            self._GameBoard[self.PosX][self.temp] = 2
                            print(self.PosX, end=',')
                            print(self.PosY)
                            sys.stdout.flush()
                            self.print_Tab(self._maxsize)
                        #if self.temp == self._maxsize:
                        #    self.temp = 0
                        print(temp)
                        self.temp = self.temp + 1
        return self._GameBoard

    def Call_Brain(self):
        self.BrainMove()
