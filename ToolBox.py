#!/usr/local/bin/python3

class Spliting:

    def __init__(self, src: str, separator: list):
        self._src = src
        self._separator = separator

    def inputsplit(self):
        savesplit = [self._src]
        for sepa in self._separator:
            self._src, savesplit = savesplit, []
            for seq in self._src:
                savesplit += seq.split(sepa)
        return savesplit


