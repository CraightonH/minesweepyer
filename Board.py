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
    FLAG = 9

class Board:
    COLS = 8
    ROWS = 8
    mine_percentage = .156
    mine_locations = set()
    solutionBoard = dict()
    gameBoard = dict()
    flag_locations = set()
    gameOver = False

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
        #print(self.toString(hidden=False))
        
    def generateMineLocations(self):
        print("generating mine locations...")
        while len(self.mine_locations) < self.max_mines:
            randcol = random.randint(0, self.COLS - 1)
            randrow = random.randint(0, self.ROWS - 1)
            self.mine_locations.add((randrow, randcol))

    def generateBoardHints(self):
        print("generating board hints...")
        for i in range(self.ROWS):
            for j in range(self.COLS):
                self.solutionBoard[i, j] = Terms.ZERO.value
                self.gameBoard[i, j] = "?"
        for loc in self.mine_locations:
            self.solutionBoard[loc] = "*"
            self.iterateHints(loc)

    def iterateHints(self, loc):
        if (loc[0], loc[1] + 1) not in self.mine_locations and loc[1] + 1 < self.COLS:
            self.solutionBoard[loc[0], loc[1] + 1] += 1
        if (loc[0], loc[1] - 1) not in self.mine_locations and loc[1] - 1 > -1:
            self.solutionBoard[loc[0], loc[1] - 1] += 1
        if (loc[0] - 1, loc[1]) not in self.mine_locations and loc[0] - 1 > -1:
            self.solutionBoard[loc[0] - 1, loc[1]] += 1
        if (loc[0] + 1, loc[1]) not in self.mine_locations and loc[0] + 1 < self.ROWS:
            self.solutionBoard[loc[0] + 1, loc[1]] += 1
        if (loc[0] - 1, loc[1] - 1) not in self.mine_locations and loc[0] - 1 > -1 and loc[1] - 1 > -1:
            self.solutionBoard[loc[0] - 1, loc[1] - 1] += 1
        if (loc[0] - 1, loc[1] + 1) not in self.mine_locations and loc[0] - 1 > -1 and loc[1] + 1 < self.COLS:
            self.solutionBoard[loc[0] - 1, loc[1] + 1] += 1
        if (loc[0] + 1, loc[1] - 1) not in self.mine_locations and loc[0] + 1 < self.ROWS and loc[1] - 1 > -1:
            self.solutionBoard[loc[0] + 1, loc[1] - 1] += 1
        if (loc[0] + 1, loc[1] + 1) not in self.mine_locations and loc[0] + 1 < self.ROWS and loc[1] + 1 < self.COLS:
            self.solutionBoard[loc[0] + 1, loc[1] + 1] += 1

    def toString(self, board=gameBoard):
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
                        retString += str(board[i, h]) 
                        retString += "  "
                        if h == self.COLS-1:
                            retString += "|"
        retString += "+"
        return retString

    def addFlag(self, location):
        self.flag_locations.add(location)

    def boardNotComplete(self):
        return not self.flag_locations == self.mine_locations

    def findZeroes(self, location):
        if location in self.solutionBoard:
            if self.solutionBoard[location] == 0 and self.gameBoard[location] == "?":
                print("found 0 at " + str(location))
                self.gameBoard[location] = self.solutionBoard[location]
                # right
                self.findZeroes((location[0], location[1] + 1))
                # left
                self.findZeroes((location[0], location[1] - 1))
                # down
                self.findZeroes((location[0] + 1,location[1]))
                # up
                self.findZeroes((location[0] - 1,location[1]))

    def revealLocation(self, location):
        if location in self.solutionBoard:
            if self.solutionBoard[location] == "*":
                self.gameOver = True
                print(self.toString(board=self.solutionBoard))
            else:
                self.findZeroes(location)
                self.gameBoard[location] = self.solutionBoard[location]
                print(self.toString())
        else:
            print("Location doesn't exist")

    def debugInfo(self):
        print("COLS: ", self.COLS)
        print("ROWS: ", self.ROWS)
        print("max_mines: ", self.max_mines)
        print("mine_locations: ", self.mine_locations)
        print("board: ", self.solutionBoard)