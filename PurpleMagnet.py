from GameLogic import *
from Magnet import Magnet
from wall import Wall
from Win import Win


class PurpleMagnet(Magnet):
    name = "purple"
    def __init__(self, currentPosition):
        super().__init__(currentPosition) 
    
    def Move(self,newPosition,grid):
        rows,colms = newPosition
        print(grid[rows,colms])
           
        if isinstance(grid[rows][colms], Magnet) or isinstance(grid[rows][colms], Wall):
            return
        else:
            oldRows,oldColms = self.currentPosition
            grid[oldRows,oldColms] = None
            self.ChangePosition(newPosition)
            grid[rows,colms] = self
            directions = [
                (1, 0),  #up
                (-1, 0),  #down
                (0,+1),  #right
                (0,-1)   #left
            ]
        for direction in directions:
        
          xOffset, yOffset = direction
          
          new_rows = rows + xOffset
          new_colms = colms + yOffset
          print(new_rows,new_colms)
          if self.is_within_bounds(new_rows, new_colms, grid):
            magnet = grid[new_rows,new_colms]   
            if isinstance(magnet, Magnet):
                print(magnet,direction)
                magnet.Push(direction, grid)
                return
            