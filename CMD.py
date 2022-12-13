#!/usr/local/bin/python3

from COMMANDES.START import START
from COMMANDES.TURN import TURN
from COMMANDES.Error_Input import ERROR
from COMMANDES.BEGIN import BEGIN
from ToolBox import Spliting
from COMMANDES.BOARD import BOARD
import sys as sys


class Cmd:
    def __init__(self):
        self.boardGame = []
        self.size = None
        self.commande = None
        self.MaxSize = None

    def print_Tab(self, size: int):
        i = 0
        for line in range(size):
            i = i + 1
            print(self.boardGame[line])

    def input(self):
        while True:
            myCMD = input()
            self.commande = Spliting(myCMD, [' ', ',']).inputsplit()

            match self.commande[0]:
                case "START":
                    if len(self.commande) == 2:
                        err = ERROR(self.commande[1]).CheckError()
                        if err == 0 and int(self.commande[1]) >= 5:
                            self.boardGame = START(int(self.commande[1])).CreatMyBoard()
                            print("OK")
                            sys.stdout.flush()
                            self.size = int(self.commande[1])
                        else:
                            print("ERROR bad START parameter")
                            sys.stdout.flush()
                    else:
                        print("ERROR bad START parameter")
                        sys.stdout.flush()
                case "TURN":
                    if len(self.commande) == 3:
                        err_arg1 = ERROR(self.commande[1]).CheckError()
                        err_arg2 = ERROR(self.commande[2]).CheckError()
                        if err_arg1 == 0 and err_arg2 == 0:
                            TURN(self.boardGame, int(self.commande[1]), int(self.commande[2]), self.size).run()
                case "END":
                    sys.exit(0)
                case "BOARD":
                    BOARD(self.boardGame, self.size).AddPositionIA()
                case "BEGIN":
                    begin = BEGIN(self.boardGame, self.size)
                    begin.run()
                case "PRINT":
                    self.print_Tab(self.size)
                case _:
                    print("UNKNOWN")
                    sys.stdout.flush()

    def run(self):
        self.input()