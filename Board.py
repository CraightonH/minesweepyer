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
        retString = " " * 7
        for i in range(self.COLS):
            space_multiplier = 5
            if i > 7:
                space_multiplier = 4
            retString += str(i + 1) + " " * space_multiplier
        for i in range(self.ROWS):
            space_multiplier = 4
            retString += "\n"
            retString += " " * space_multiplier
            for j in range(self.COLS):
                retString += "+"
                if j < self.COLS:
                    retString += "-----"
                if i < self.ROWS and j == self.COLS - 1:
                    retString += "+\n"
                    for h in range(self.COLS):
                        if h == 0:
                            retString += " "
                            if i < 9:
                                retString += " "
                            retString += str(i + 1)
                            retString += " "
                        retString += "|  "
                        retString += str(board[i, h]) 
                        retString += "  "
                        if h == self.COLS-1:
                            retString += "|"
        # print final row border
        retString += "\n    "
        retString += "+-----" * self.COLS
        retString += "+"
        return retString

    def addFlag(self, location):
        if location not in self.flag_locations:
            self.flag_locations.add(location)
            self.gameBoard[location] = "F"
        else:
            self.flag_locations.discard(location)
            self.gameBoard[location] = "?"
        print(self.toString())

    def notComplete(self):
        return not self.flag_locations == self.mine_locations

    def findFrontline(self, location, checkedLocations=set()):
        if location in self.solutionBoard:
            # uncover this square
            self.gameBoard[location] = self.solutionBoard[location]
            # is this not a 0? then stop
            checkedLocations.add(location)
            if self.gameBoard[location] != 0:
                return
            # am I a 0 and touching a 0? then continue
            if      ((location[0], location[1] + 1) in self.solutionBoard and self.solutionBoard[location[0], location[1] + 1] == 0) \
                or  ((location[0], location[1] - 1) in self.solutionBoard and self.solutionBoard[location[0], location[1] - 1] == 0) \
                or  ((location[0] + 1, location[1]) in self.solutionBoard and self.solutionBoard[location[0] + 1, location[1]] == 0) \
                or  ((location[0] - 1, location[1]) in self.solutionBoard and self.solutionBoard[location[0] - 1, location[1]] == 0) \
                and self.gameBoard[location] == 0:
                # return
            # if self.solutionBoard[location] == 0 and self.gameBoard[location] == "?":
            #     # print("found 0 at " + str(location))
                # right
                if (location[0], location[1] + 1) not in checkedLocations:
                    self.findFrontline((location[0], location[1] + 1), checkedLocations)
                # left
                if (location[0], location[1] - 1) not in checkedLocations:
                    self.findFrontline((location[0], location[1] - 1), checkedLocations)
                # down
                if (location[0] + 1,location[1]) not in checkedLocations:
                    self.findFrontline((location[0] + 1,location[1]), checkedLocations)
                # up
                if (location[0] - 1,location[1]) not in checkedLocations:
                    self.findFrontline((location[0] - 1,location[1]), checkedLocations)

    def uncoverSafeLocations(self, loc):
        # check for current location being flag
        if self.gameBoard[loc] == "F":
            print("Cannot uncover at a flag!")
            return
        # check for current location being unknown
        elif self.gameBoard[loc] == "?":
            print("Cannot uncover at an unknown coordinate!")
            return
        if self.gameBoard[loc] == 0:
            self.findFrontline(loc)
            return
        # check for any surrounding location being on the board AND a mine AND the gameboard does not have it flagged - game over
        if      (loc[0], loc[1] + 1) in self.solutionBoard and self.solutionBoard[loc[0], loc[1] + 1] == "*" and not self.gameBoard[loc[0], loc[1] + 1] == "F" \
            or  (loc[0], loc[1] - 1) in self.solutionBoard and self.solutionBoard[loc[0], loc[1] - 1] == "*" and not self.gameBoard[loc[0], loc[1] - 1] == "F" \
            or (loc[0] - 1, loc[1]) in self.solutionBoard and self.solutionBoard[loc[0] - 1, loc[1]] == "*" and not self.gameBoard[loc[0] - 1, loc[1]] == "F" \
            or (loc[0] + 1, loc[1]) in self.solutionBoard and self.solutionBoard[loc[0] + 1, loc[1]] == "*" and not self.gameBoard[loc[0] + 1, loc[1]] == "F" \
            or (loc[0] - 1, loc[1] - 1) in self.solutionBoard and self.solutionBoard[loc[0] - 1, loc[1] - 1] == "*" and not self.gameBoard[loc[0] - 1, loc[1] - 1] == "F" \
            or (loc[0] - 1, loc[1] + 1) in self.solutionBoard and self.solutionBoard[loc[0] - 1, loc[1] + 1] == "*" and not self.gameBoard[loc[0] - 1, loc[1] + 1] == "F" \
            or (loc[0] + 1, loc[1] - 1) in self.solutionBoard and self.solutionBoard[loc[0] + 1, loc[1] - 1] == "*" and not self.gameBoard[loc[0] + 1, loc[1] - 1] == "F" \
            or (loc[0] + 1, loc[1] + 1) in self.solutionBoard and self.solutionBoard[loc[0] + 1, loc[1] + 1] == "*" and not self.gameBoard[loc[0] + 1, loc[1] + 1] == "F" :
            self.setGameOver()
            return
        # check for any surrounding location being on the board AND unknown - uncover
        if (loc[0], loc[1] + 1) in self.gameBoard and self.gameBoard[loc[0], loc[1] + 1] == "?":
            self.gameBoard[loc[0], loc[1] + 1] = self.solutionBoard[loc[0], loc[1] + 1]
        if (loc[0], loc[1] - 1) in self.gameBoard and self.gameBoard[loc[0], loc[1] - 1] == "?":
            self.gameBoard[loc[0], loc[1] - 1] = self.solutionBoard[loc[0], loc[1] - 1]
        if (loc[0] - 1, loc[1]) in self.gameBoard and self.gameBoard[loc[0] - 1, loc[1]] == "?":
            self.gameBoard[loc[0] - 1, loc[1]] = self.solutionBoard[loc[0] - 1, loc[1]]
        if (loc[0] + 1, loc[1]) in self.gameBoard and self.gameBoard[loc[0] + 1, loc[1]] == "?":
            self.gameBoard[loc[0] + 1, loc[1]] = self.solutionBoard[loc[0] + 1, loc[1]]
        if (loc[0] - 1, loc[1] - 1) in self.gameBoard and self.gameBoard[loc[0] - 1, loc[1] - 1] == "?":
            self.gameBoard[loc[0] - 1, loc[1] - 1] = self.solutionBoard[loc[0] - 1, loc[1] - 1]
        if (loc[0] - 1, loc[1] + 1) in self.gameBoard and self.gameBoard[loc[0] - 1, loc[1] + 1] == "?":
            self.gameBoard[loc[0] - 1, loc[1] + 1] = self.solutionBoard[loc[0] - 1, loc[1] + 1]
        if (loc[0] + 1, loc[1] - 1) in self.gameBoard and self.gameBoard[loc[0] + 1, loc[1] - 1] == "?":
            self.gameBoard[loc[0] + 1, loc[1] - 1] = self.solutionBoard[loc[0] + 1, loc[1] - 1]
        if (loc[0] + 1, loc[1] + 1) in self.gameBoard and self.gameBoard[loc[0] + 1, loc[1] + 1] == "?":
            self.gameBoard[loc[0] + 1, loc[1] + 1] = self.solutionBoard[loc[0] + 1, loc[1] + 1]
        print(self.toString())

    def revealLocation(self, location):
        if location in self.solutionBoard:
            if self.solutionBoard[location] == "*":
                self.setGameOver()
            else:
                self.findFrontline(location)
                self.gameBoard[location] = self.solutionBoard[location]
                print(self.toString())
        else:
            print("Location doesn't exist")

    def setGameOver(self):
        self.gameOver = True
        print(self.toString(board=self.solutionBoard))

    def debugInfo(self):
        print("COLS: ", self.COLS)
        print("ROWS: ", self.ROWS)
        print("max_mines: ", self.max_mines)
        print("mine_locations: ", self.mine_locations)
        print("board: ", self.solutionBoard)