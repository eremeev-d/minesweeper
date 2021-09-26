import os
import sys
import random
import pickle
from Game import Game


def save_game(game, filename):
    with open('saves/{}'.format(filename), 'wb') as f:
        pickle.dump(game, f)


def load_game(filename):
    with open('saves/{}'.format(filename), 'rb') as f:
        return pickle.load(f)


os.system("cls")
print("Enter \"Start HEIGHT WIDTH BOMBS\" to start a new game")
print("Enter \"Load FILENAME \" to load a game")
command = input().split()
if command[0] == "Start":
    height, width, bombs = int(command[1]), int(command[2]), int(command[3])
    game = Game(height, width, bombs)
elif command[0] == "Load":
    game = load_game(command[1])
else:
    print("Not a correct comand")
    sys.exit()
while True: # Game cycle
    game.show_map(game.user_map)
    command = input().split()
    if command[0] == "Save":
        save_game(game, command[1])
    else:
        game.make_move(int(command[1])-1, int(command[0])-1, command[2])