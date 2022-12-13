import numpy
from os import system

srcs = [
    "main.py",
    "CMD.py",
    "ToolBox.py",
    "Parsing.py"
]

src_dict = ""
for src in srcs:
    src_dict += " " + src

system("pip install numpy")
system("pip install pyinstaller")

system("pyinstaller" + src_dict + " --name pbrain-gomoku-ai.exe --onefile")
system('copy .\\dist\\pbrain-gomoku-ai.exe .')