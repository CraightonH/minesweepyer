import random

class Game:
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
        if cols != None: self.COLS = cols
        if rows != None: self.ROWS = rows
        self.max_mines = round(self.COLS * self.ROWS * self.mine_percentage)
        if mines != 0 and mines != None:
            self.max_mines = mines
        self.generateMineLocations()
        self.generateBoardHints()
        print("have fun!")
        print()
        # print(self.toString())
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
                self.solutionBoard[i, j] = 0
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

    def help(self, html=True):
        retString = ""
        retString += "CHOOSE"
        if html: retString += "<br />"
        retString += "Choose a box to uncover by typing a comma separated list"
        retString += "of coordinates in the form 'row,column' where 1,1 is the"
        retString += "top left most box on the board."
        if html: retString += "<br />"
        retString += "ie. '1,1'"
        if html: retString += "<br />"
        if html: retString += "<br />"
        retString += "FLAG"
        if html: retString += "<br />"
        retString += "Mark a flag by typing the letter 'f ' in front of your list."
        if html: retString += "<br />"
        retString += "ie. 'f 2,2'"
        if html: retString += "<br />"
        if html: retString += "<br />"
        retString += "UNCOVER"
        if html: retString += "<br />"
        retString += "Uncover safe boxes by typing 'u ' before your coordinates and select"
        retString += "a square that touches a flag such that it's guaranteed to not have an unflagged mine next to it."
        retString += "If you uncover at a coordinate that is not guaranteed to be safe and"
        retString += "a mine is uncovered in the process, game over!"
        if html: retString += "<br />"
        retString += "ie. 'u 1,1'"
        return retString

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
                or  ((location[0] - 1, location[1] - 1) in self.solutionBoard and self.solutionBoard[location[0] - 1, location[1] - 1] == 0) \
                or  ((location[0] - 1, location[1] + 1) in self.solutionBoard and self.solutionBoard[location[0] - 1, location[1] + 1] == 0) \
                or  ((location[0] + 1, location[1] - 1) in self.solutionBoard and self.solutionBoard[location[0] - 1, location[1] - 1] == 0) \
                or  ((location[0] + 1, location[1] + 1) in self.solutionBoard and self.solutionBoard[location[0] - 1, location[1] + 1] == 0) \
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
                # top-left
                if (location[0] - 1, location[1] - 1) not in checkedLocations:
                    self.findFrontline((location[0] - 1, location[1] - 1), checkedLocations)
                # top-right
                if (location[0] - 1, location[1] + 1) not in checkedLocations:
                    self.findFrontline((location[0] - 1, location[1] + 1), checkedLocations)
                # bottom-left
                if (location[0] + 1,location[1] - 1) not in checkedLocations:
                    self.findFrontline((location[0] + 1,location[1] - 1), checkedLocations)
                # bottom-right
                if (location[0] + 1,location[1] + 1) not in checkedLocations:
                    self.findFrontline((location[0] + 1,location[1] + 1), checkedLocations)
            return True
        return False

    def uncoverSafeLocations(self, loc):
        if loc in self.solutionBoard:
            # check for current location being flag
            if self.gameBoard[loc] == "F":
                print("Cannot uncover at a flag!")
                return False
            # check for current location being unknown
            elif self.gameBoard[loc] == "?":
                print("Cannot uncover at an unknown coordinate!")
                return False
            if self.gameBoard[loc] == 0:
                self.findFrontline(loc)
                return False
            # check for any surrounding location being on the board AND a mine AND the gameboard does not have it flagged - game over
            if      (loc[0], loc[1] + 1) in self.solutionBoard and self.solutionBoard[loc[0], loc[1] + 1] == "*" and not self.gameBoard[loc[0], loc[1] + 1] == "F" \
                or  (loc[0], loc[1] - 1) in self.solutionBoard and self.solutionBoard[loc[0], loc[1] - 1] == "*" and not self.gameBoard[loc[0], loc[1] - 1] == "F" \
                or (loc[0] - 1, loc[1]) in self.solutionBoard and self.solutionBoard[loc[0] - 1, loc[1]] == "*" and not self.gameBoard[loc[0] - 1, loc[1]] == "F" \
                or (loc[0] + 1, loc[1]) in self.solutionBoard and self.solutionBoard[loc[0] + 1, loc[1]] == "*" and not self.gameBoard[loc[0] + 1, loc[1]] == "F" \
                or (loc[0] - 1, loc[1] - 1) in self.solutionBoard and self.solutionBoard[loc[0] - 1, loc[1] - 1] == "*" and not self.gameBoard[loc[0] - 1, loc[1] - 1] == "F" \
                or (loc[0] - 1, loc[1] + 1) in self.solutionBoard and self.solutionBoard[loc[0] - 1, loc[1] + 1] == "*" and not self.gameBoard[loc[0] - 1, loc[1] + 1] == "F" \
                or (loc[0] + 1, loc[1] - 1) in self.solutionBoard and self.solutionBoard[loc[0] + 1, loc[1] - 1] == "*" and not self.gameBoard[loc[0] + 1, loc[1] - 1] == "F" \
                or (loc[0] + 1, loc[1] + 1) in self.solutionBoard and self.solutionBoard[loc[0] + 1, loc[1] + 1] == "*" and not self.gameBoard[loc[0] + 1, loc[1] + 1] == "F" :
                return self.setGameOver()
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
            # print(self.toString())
            return True
        return False

    def addFlag(self, location):
        if location in self.solutionBoard:
            if location not in self.flag_locations:
                self.flag_locations.add(location)
                self.gameBoard[location] = "F"
            else:
                self.flag_locations.discard(location)
                self.gameBoard[location] = "?"
            return True
        return False
        # print(self.toString())

    def revealLocation(self, location):
        result = False
        if location in self.solutionBoard:
            if self.solutionBoard[location] == "*":
                result = self.setGameOver()
            else:
                result = self.findFrontline(location)
                self.gameBoard[location] = self.solutionBoard[location]
        return result

    def setGameOver(self):
        self.gameOver = True
        return self.gameOver

    def debugInfo(self):
        print("COLS: ", self.COLS)
        print("ROWS: ", self.ROWS)
        print("max_mines: ", self.max_mines)
        print("mine_locations: ", self.mine_locations)
        print("board: ", self.solutionBoard)

    #### API Helpers

    def remap_tuple_keys_as_strings(self, dict):
        return [{'key': k, 'value': v} for k, v in dict.items()]

    def getGameBoard(self):
        return self.remap_tuple_keys_as_strings(self.gameBoard)

    def getSolutionBoard(self):
        return self.remap_tuple_keys_as_strings(self.solutionBoard)