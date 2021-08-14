from Board import Board

print("How to play:")
print("Choose a box to uncover by typing a comma separated list")
print("of coordinates in the form 'row,column' where 1,1 is the")
print("top left most box on the board.")
print("Mark a flag by typing the letter 'f' in front of your list.")
print("ie. 'f 1,1'")
print("Uncover safe boxes by typing 'u ' before your coordinates and select")
print("a square that touches a flag such that it's guaranteed to not have an unflagged mine next to it.")
print("If you uncover at a coordinate that is not guaranteed to be safe and")
print("a mine is uncovered in the process, game over!")
print()

board = Board()
# board.debugInfo()
while(board.notComplete() and not board.gameOver):
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
    print("BOOM!!! Game over!")
else:
    print("Congratulations! You win!")