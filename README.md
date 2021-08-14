# minesweepyer

A python minesweeper game.

Here's some output with the game board hidden:
```
$ python game.py
How to play:
Choose a box to uncover by typing a comma separated list
of coordinates in the form 'row,column' where 1,1 is the
top left most box on the board.
Mark a flag by typing the letter 'f' in front of your list.
ie. 'f 1,1'
Uncover safe boxes by typing 'u ' before your coordinates and select
a square that touches a flag such that it's guaranteed to not have an unflagged mine next to it.    
If you uncover at a coordinate that is not guaranteed to be safe and
a mine is uncovered in the process, game over!

calculating difficulty...
generating mine locations...
generating board hints...
have fun!
       1     2     3     4     5     6     7     8
    +-----+-----+-----+-----+-----+-----+-----+-----+
  1 |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
  2 |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
  3 |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
  4 |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
  5 |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
  6 |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
  7 |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
  8 |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
Choose a box to uncover:
```
And the unlucky loser:
```
       1     2     3     4     5     6     7     8     
    +-----+-----+-----+-----+-----+-----+-----+-----+  
  1 |  0  |  0  |  0  |  0  |  0  |  2  |  *  |  2  |  
    +-----+-----+-----+-----+-----+-----+-----+-----+  
  2 |  0  |  1  |  1  |  1  |  0  |  2  |  *  |  2  |  
    +-----+-----+-----+-----+-----+-----+-----+-----+  
  3 |  0  |  1  |  *  |  1  |  0  |  1  |  2  |  2  |  
    +-----+-----+-----+-----+-----+-----+-----+-----+  
  4 |  0  |  1  |  1  |  1  |  0  |  0  |  1  |  *  |  
    +-----+-----+-----+-----+-----+-----+-----+-----+  
  5 |  0  |  0  |  1  |  2  |  2  |  2  |  2  |  2  |  
    +-----+-----+-----+-----+-----+-----+-----+-----+  
  6 |  1  |  1  |  2  |  *  |  *  |  3  |  *  |  2  |  
    +-----+-----+-----+-----+-----+-----+-----+-----+  
  7 |  *  |  1  |  2  |  *  |  3  |  3  |  *  |  2  |  
    +-----+-----+-----+-----+-----+-----+-----+-----+  
  8 |  1  |  1  |  1  |  1  |  1  |  1  |  1  |  1  |  
    +-----+-----+-----+-----+-----+-----+-----+-----+
BOOM!!! Game over!
```