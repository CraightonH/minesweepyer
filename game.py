from Board import Board

board = Board()
# board.debugInfo()
while(board.boardNotComplete() and not board.gameOver):
    location = input()
    location = tuple(map(int, location.split(',')))
    board.revealLocation(location)

if board.gameOver:
    print("BOOM!!! Game over!")
else:
    print("Congratulations! You win!")