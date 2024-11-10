
import numpy as np
from GameLogic import parseInput, checkIndices, check_Win_Positions
from Level import Level
from PurpleMagnet import PurpleMagnet
from RedMagnet import RedMagnet

level_number = int(input("Insert level number: "))
gameGrid, tries = Level.LoadLevel(level_number)
print(gameGrid)

userInput = input("Enter the indices in the format (1,2),(3,4): ")
indices = parseInput(userInput)
initialPosition = indices[0]
rows, colms = initialPosition
newPosition = indices[1]
nRows, nColms = newPosition

initialMagnet = checkIndices(rows, colms, gameGrid)
if isinstance(initialMagnet, (PurpleMagnet, RedMagnet)):
    initialMagnet.Move(newPosition, gameGrid)
else:
    print("Can't move")
print(gameGrid)

winPositions = np.argwhere(check_win_positions(gameGrid))

while winPositions.size > 0 and tries > 0:
    tries -= 1
    print("Remaining tries:", tries)

    userInput = input("(x,y),(new_x,new_y): ")
    indices = parseInput(userInput)
    initialPosition = indices[0]
    rows, colms = initialPosition
    newPosition = indices[1]
    nRows, nColms = newPosition

    initialMagnet = checkIndices(rows, colms, gameGrid)
    if isinstance(initialMagnet, (PurpleMagnet, RedMagnet)):
        initialMagnet.Move(newPosition, gameGrid)
    else:
        print("Can't move")
    
    print(gameGrid)

 
    winPositions = np.argwhere(check_win_positions(gameGrid))
    

if winPositions.size == 0:
    print("You won!")
else:
    print("No more tries left. Game over!")
    