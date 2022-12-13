#!/usr/local/bin/python3

import random as rd
import sys as sys
import time as tm
from ToolBox import Spliting
from COMMANDES.Error_Input import ERROR
from my_brain import BRAIN

class BOARD:
    def __init__(self, GameBoard, maxsize):
        self._GameBoard = GameBoard
        self.myList = None
        self.PosX = None
        self.PosY = None
        self._maxsize = maxsize
        self.NewBoard = []

    def movePlayer(self, posx: int, posy: int):
        self._GameBoard[posx][posy] = 2
        return self._GameBoard

    def moveBrain(self, posx: int, posy: int):
        #BRAIN(self._GameBoard, self._maxsize)
        self._GameBoard[posx][posy] = 1
        return self._GameBoard

    def IaPlay(self, posx: int, posy: int):
        self.NewBoard = BRAIN(self._GameBoard, self._maxsize).Call_Brain()
        #self._GameBoard[posx][posy] = 1
        #print(posx, end=',')
        #print(posy)
        #sys.stdout.flush()
        return self.NewBoard


    def VerifPosForBoard(self):
        self.PosX = rd.randrange(0, self._maxsize-1)
        self.PosY = rd.randrange(0, self._maxsize-1)

        match self._GameBoard[self.PosX][self.PosY]:

            case 1:
                self.PosX = rd.randrange(0, self._maxsize-1)
                self.PosY = rd.randrange(0, self._maxsize-1)
            case 2:
                self.PosX = rd.randrange(0, self._maxsize-1)
                self.PosY = rd.randrange(0, self._maxsize-1)
            case 0:
                self.IaPlay(self.PosX, self.PosY)

    def AddPositionIA(self):
        while True:
            myCMD = input()
            if len(myCMD) > 0:
                self.myList = Spliting(myCMD, [' ', ',']).inputsplit()
                if self.myList[0] == "DONE":
                    self.VerifPosForBoard()
                    break
                else:
                    if ERROR(self.myList[0]).CheckError() == 0 and ERROR(self.myList[1]).CheckError() == 0:
                        match self.myList[2]:
                            case '1':
                                self.moveBrain(int(self.myList[0]), int(self.myList[1]))
                            case '2':
                                self.movePlayer(int(self.myList[0]), int(self.myList[1]))
            if len(myCMD) == 0:
                tm.sleep(1)