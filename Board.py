from enum import Enum 
import random

class Terms(Enum):
    MINE = -1
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    FLAG = 10

class Board:
    COLS = 8
    ROWS = 8
    mine_percentage = .156
    mine_locations = set()
    board = dict()

    def __init__(self, cols=8, rows=8, mines=0):
        print("calculating difficulty...")
        self.COLS = cols
        self.ROWS = rows
        self.max_mines = round(self.COLS * self.ROWS * self.mine_percentage)
        if (mines != 0):
            self.max_mines = mines
        self.generateMineLocations()
        self.generateBoardHints()
        print("have fun!")
        print(self.toString())
        print(self.toString(hidden=False))
        
    def generateMineLocations(self):
        print("generating mine locations...")
        while len(self.mine_locations) < self.max_mines:
            randx = random.randint(0, self.COLS - 1)
            randy = random.randint(0, self.ROWS - 1)
            self.mine_locations.add((randx, randy))

    def generateBoardHints(self):
        print("generating board hints...")
        for i in range(self.ROWS):
            for j in range(self.COLS):
                self.board[i, j] = Terms.ZERO.value
        for loc in self.mine_locations:
            self.board[loc] = "*"
            self.iterateHints(loc)

    def iterateHints(self, loc):
        if (loc[0], loc[1] + 1) not in self.mine_locations and loc[1] + 1 < self.COLS:
            self.board[loc[0], loc[1] + 1] += 1
        if (loc[0], loc[1] - 1) not in self.mine_locations and loc[1] - 1 > -1:
            self.board[loc[0], loc[1] - 1] += 1
        if (loc[0] - 1, loc[1]) not in self.mine_locations and loc[0] - 1 > -1:
            self.board[loc[0] - 1, loc[1]] += 1
        if (loc[0] + 1, loc[1]) not in self.mine_locations and loc[0] + 1 < self.ROWS:
            self.board[loc[0] + 1, loc[1]] += 1
        if (loc[0] - 1, loc[1] - 1) not in self.mine_locations and loc[0] - 1 > -1 and loc[1] - 1 > -1:
            self.board[loc[0] - 1, loc[1] - 1] += 1
        if (loc[0] - 1, loc[1] + 1) not in self.mine_locations and loc[0] - 1 > -1 and loc[1] + 1 < self.COLS:
            self.board[loc[0] - 1, loc[1] + 1] += 1
        if (loc[0] + 1, loc[1] - 1) not in self.mine_locations and loc[0] + 1 < self.ROWS and loc[1] - 1 > -1:
            self.board[loc[0] + 1, loc[1] - 1] += 1
        if (loc[0] + 1, loc[1] + 1) not in self.mine_locations and loc[0] + 1 < self.ROWS and loc[1] + 1 < self.COLS:
            self.board[loc[0] + 1, loc[1] + 1] += 1

    def toString(self, hidden=True):
        retString = ""
        for i in range(self.ROWS):
            retString += "\n"
            for j in range(self.COLS):
                retString += "+"
                if j < self.COLS:
                    retString += "-----"
                if i < self.ROWS - 1 and j == self.COLS - 1:
                    retString += "+\n"
                    for h in range(self.COLS):
                        retString += "|  " 
                        if hidden:
                            retString += "?" 
                        else:
                            retString += str(self.board[i, h]) 
                        retString += "  "
                        if h == self.COLS-1:
                            retString += "|"
        retString += "+"
        return retString

    def debugInfo(self):
        print("COLS: ", self.COLS)
        print("ROWS: ", self.ROWS)
        print("max_mines: ", self.max_mines)
        print("mine_locations: ", self.mine_locations)
        print("board: ", self.board)