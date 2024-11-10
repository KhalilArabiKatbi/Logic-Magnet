from multipledispatch import dispatch

from GameLogic import *
from wall import Wall


class Magnet:
      lastPosition = None
      currentPosition = None
      interactable = False
      name = "magnet"
      def __init__(self,currentPosition):
            self.currentPosition = currentPosition
      def __repr__(self):
            return self.name
      @dispatch(int,int)      
      def ChangePosition(self,newX,newY):      
            self.lastPosition = self.currentPosition
            self.currentPosition = newX,newY
      @dispatch(tuple)      
      def ChangePosition(self,newPosition):
            newX,newY = newPosition
            self.ChangePosition(newX,newY)
      def Push(self,direction,grid):
            x,y = direction
            rows,colms = self.currentPosition
            print(rows,colms)
            print("next is",grid[rows+x,colms+y])
            if not self.is_within_bounds(rows + x,colms+ y, grid):
                 print("can't move out of bounds") 
                 return False
            if(isinstance(grid[rows + x,colms+ y], Wall)):
                  print("can't move there is a wall")
                  return False
            elif(isinstance(grid[rows + x,colms+ y] , Magnet)):
                  print("found magnet",grid[rows+x,colms+y])
                  nextMagnet = grid[rows+x,colms+y]
                  if(nextMagnet.Move(direction,grid)):
                        self.ChangePosition(rows+x,colms+y)
                        grid[rows+x,colms+y] = grid[rows,colms]
                        grid[rows,colms] = None
                        return
            elif(isinstance(grid[rows + x,colms+ y] , (Magnet,Win))):
                  print("will move there is nothing")
                  self.ChangePosition(rows+x,colms+y)
                  grid[rows+x,colms+y] = grid[rows,colms]
                  grid[rows,colms] = None   
                  return True        
      def Pull(self,direction,grid):
            x,y = direction
            rows,colms = self.currentPosition
            if(isinstance(grid[rows + x,colms+ y],Wall)or(not self.is_within_bounds(rows + x,colms+ y, grid))):
                  return 
            elif(isinstance(grid[rows + x,colms+ y] , (Magnet,Win))):
                  newDirection = increase(x),increase(y)
                  self.Pull(newDirection,grid)
            elif(isinstance(grid[rows + x,colms+ y] ,Magnet)):
                 foundMagnet = checkIndices(rows+x,colms+y) 
                 grid[rows+x,colms+y] = None
                 foundMagnet.ChangePosition(rows,colms)
                 grid[rows,colms]= foundMagnet
                 newDirection = increase(x),increase(y)
                 self.Pull(newDirection,grid)
                 return
      def is_within_bounds(self,rows, cols, grid):
        return 0 <= rows < len(grid) and 0 <= cols < len(grid[0])        
            