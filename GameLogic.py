import numpy as np
from multipledispatch import dispatch

from Magnet import Magnet
from PurpleMagnet import PurpleMagnet
from RedMagnet import RedMagnet
from wall import Wall
from Win import Win


def grid(i, j):
    return np.empty((i, j), dtype=object)  

def insertInGrid(gameGrid, items):
    for item in items:
        row, col = item.currentPosition 
        gameGrid[row, col] = item  
        
@dispatch(int, int, np.ndarray)
def checkIndices(rows, colms, grid):
    try:
        return grid[rows, colms]
    except IndexError as e:
        print(f"IndexError caught: {e}")
        return Wall  

@dispatch(tuple, np.ndarray)
def checkIndices(position, grid):
    rows, colms = position
    return checkIndices(rows, colms, grid)  

def increase(value):
    if value > 0:
        return value + 1  
    elif value < 0:
        return value - 1  
    else:
        return 0
def parseInput(input):
    return eval(input)
        
def is_within_bounds(rows, cols, grid):
    return 0 <= rows < len(grid) and 0 <= cols < len(grid[0])        

def check_win_positions(grid):
    return np.array([[isinstance(cell, Win) for cell in row] for row in grid])
def possibleMoves(grid):
    initialMagnet = findColoredMagnet(grid)
    
def findColoredMagnet(grid):
    indices = np.argwhere(np.isin(grid, (PurpleMagnet, RedMagnet)))
    return indices if indices.size >0 else None
def canMove(grid, row, colm):
    return (0 <= row < grid.shape[0] and 
            0 <= colm < grid.shape[1] and 
            not isinstance(grid[row, colm], (Wall, Magnet)))
