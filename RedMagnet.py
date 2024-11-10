from GameLogic import *
from Magnet import Magnet
from wall import Wall


class RedMagnet(Magnet):
    name = "red"
    def __init__(self,currentPosition):
               super().__init__(currentPosition) 

    def Move(self,newPosition,grid):
        rows,colms = newPosition
        if (isinstance([grid,colms],Magnet) or  isinstance(grid[rows][colms], Wall)):
            return
        else:
            oldRows,oldColms = self.currentPosition
            grid[oldRows,oldColms] = None
            self.ChangePosition(newPosition)
            grid[rows,colms] = self
            directions = [
                (1, 0),  
                (-1, 0),  
                (0,+1),  
                (0,-1)   
            ]
        for direction in directions:
          xOffset, yOffset = direction
          new_rows = rows + xOffset
          new_colms = colms + yOffset
          if is_within_bounds(new_rows, new_colms, grid):
            magnet = grid[new_rows,new_colms]   
            if isinstance(magnet, Magnet):
                print(magnet,direction)
                magnet.Pull(direction, grid)            
    
    