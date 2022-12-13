##
## EPITECH PROJECT, 2022
## gomoku
## File description:
## Makefile
##

all:
	cp main.py pbrain-gomoku-ai
	chmod +x main.py CMD.py ToolBox.py
	chmod +x pbrain-gomoku-ai

install:
		(cd venv)
		bin/activate

clean:

fclean: clean
		rm pbrain-gomoku-ai

re: fclean all