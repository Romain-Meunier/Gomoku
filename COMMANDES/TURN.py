#!/usr/local/bin/python3

import random as rd
import sys as sys

class TURN:
    def __init__(self, GameBoard, Posx: int, Posy: int, MaxRand: int):
        self._GameBoard = GameBoard
        self._Posx = Posx
        self._Posy = Posy
        self.maxRand = MaxRand
        self.MyPosX = None
        self.MyPosY = None


    def PlayerPose(self):
        self._GameBoard[self._Posx][self._Posy] = 2
        return self._GameBoard

    def IaPlay(self, posx: int, posy: int):
        self._GameBoard[posx][posy] = 1
        print(posx, end=',')
        print(posy)
        sys.stdout.flush()
        return self._GameBoard


    def VerifPos(self):
        self.MyPosX = rd.randrange(0, self.maxRand-1)
        self.MyPosY = rd.randrange(0, self.maxRand-1)

        match self._GameBoard[self.MyPosX][self.MyPosY]:

            case 1:
                self.MyPosX = rd.randrange(0, self.maxRand-1)
                self.MyPosY = rd.randrange(0, self.maxRand-1)
            case 2:
                self.MyPosX = rd.randrange(0, self.maxRand-1)
                self.MyPosY = rd.randrange(0, self.maxRand-1)
            case 0:
                self.IaPlay(self.MyPosX, self.MyPosY)

    def run(self):
        self.PlayerPose()
        self.VerifPos()

