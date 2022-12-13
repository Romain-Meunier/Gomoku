#!/usr/local/bin/python3
import sys as sys

class START:
    def __init__(self, sizeBoard: int):
        self._sizeBoard = sizeBoard
        self._theBoard = self.CreatMyBoard()

    def CreatMyBoard(self):
        my_Board = [[0 for j in range(self._sizeBoard)] for i in range(self._sizeBoard)]
        return my_Board
