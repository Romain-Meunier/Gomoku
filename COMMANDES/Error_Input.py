#!/usr/local/bin/python3

import sys as sys

class ERROR:
    def __init__(self, nbr: str):
        self._nbr = nbr

    def CheckError(self):
        if self._nbr.isdigit():
            return 0
        else:
            return 84
