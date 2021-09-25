import os
import sys
import random

class Game:    
    def __init__(self, width = 5, height = 5, bombs = 5):
        if bombs > width*height:
            print("Too many bombs")
            sys.exit()
        self.width = width
        self.height = height
        self.bombs = bombs
        self.bomb_map = self._generate_bomb_map()
        self.user_map = [['#' for _ in range(self.width)] for _ in range(self.height)]

    def _generate_bomb_map(self):
        bomb_map = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for _ in range(self.bombs):
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            while bomb_map[x][y] == 1:
                x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            bomb_map[x][y] = 1
        return bomb_map

    def game_over(self):
        print("Game over")
        print()
        print("User map:")
        self.show_user_map(cls=False)
        print()
        print("Bomb map:")
        self.show_bomb_map(cls=False)
        sys.exit()

    def show_user_map(self, cls = True):
        if cls:
            os.system('cls')
        for i in range(self.height-1, -1, -1):
            for j in range(self.width):
                print(self.user_map[i][j], end='')
            print()

    def show_bomb_map(self, cls = True):
        if cls:
            os.system('cls')
        for i in range(self.height-1, -1, -1):
            for j in range(self.width):
                print(self.bomb_map[i][j], end='')
            print()

    def _bombs_around(self, i_cell, j_cell):
        bombs_cnt = 0
        for i in range(max(i_cell-1, 0), min(i_cell+2, self.height)):
            for j in range(max(j_cell-1, 0), min(j_cell+2, self.width)):
                bombs_cnt += self.bomb_map[i][j]
        return bombs_cnt

    def open_cell(self, i_cell, j_cell):
        if (i_cell < 0) or (j_cell < 0) or (i_cell >= self.height) or (j_cell >= self.width):
            return
        if self.user_map[i_cell][j_cell] != '#':
            return
        if self.bomb_map[i_cell][j_cell] == 1:
            self.user_map[i_cell][j_cell] = '*'
            self.game_over()
        self.user_map[i_cell][j_cell] = str(self._bombs_around(i_cell, j_cell))

        if self.user_map[i_cell][j_cell] == '0':
            self.open_cell(i_cell, j_cell-1)
            self.open_cell(i_cell, j_cell+1)
            self.open_cell(i_cell-1, j_cell)
            self.open_cell(i_cell+1, j_cell)


game = Game(10, 10, 5)
while True:
    game.show_user_map()
    print()
    i, j = map(int, input().split())
    game.open_cell(i, j)