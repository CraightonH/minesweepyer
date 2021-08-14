from Board import Board
import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rows", type=int, help="How many rows on the game board to generate")
parser.add_argument("-c", "--cols", type=int, help="How many columns on the game board to generate")
parser.add_argument("-m", "--mines", type=int, help="Override default number of calculated mines")
args = parser.parse_args()

print(args.rows, args.cols, args.mines) 

board = Board(rows=args.rows, cols=args.cols, mines=args.mines)
board.help()
while(board.notComplete() and not board.gameOver):
    print(board.toString())
    location = input("Choose a box to uncover: ")
    flag = False
    uncover = False
    if "f" in location:
        location = location.replace("f ", "")
        flag = True
    if "u" in location:
        location = location.replace("u ", "")
        uncover = True
    location = tuple(map(int, location.split(','))) # split comma separated input 
    location = (location[0] - 1, location[1] - 1) # correct 1 index to 0 index
    if flag:
        board.addFlag(location)
    elif uncover:
        board.uncoverSafeLocations(location)
    else:
        board.revealLocation(location)

if board.gameOver:
    print(board.toString(board.solutionBoard))
    print("BOOM!!! Game over!")
else:
    print(board.toString(board.solutionBoard))
    print("Congratulations! You win!")