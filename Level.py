from GameLogic import *
from Magnet import Magnet
from PurpleMagnet import PurpleMagnet
from RedMagnet import RedMagnet
from Win import Win


class Level:
    levelNumber = 0
    levels = {}  
    rows,colms = 0,0
    magnets = []
    walls = []
    win = []
    tries = 0
    def __init__(self,levelNumber,rows,colms,magnets,walls,win,tries):
        self.levelNumber = levelNumber
        self.rows=rows
        self.colms=colms
        self.magnets=magnets
        self.walls=walls
        self.win = win
        self.tries = tries
        Level.levels[self.levelNumber] = self
      
    @classmethod
    def LoadLevel(cls, levelNumber):
        if levelNumber not in cls.levels:
            raise ValueError("Level is not defined.")
        else:
            level = cls.levels[levelNumber]
            gameGrid = grid(level.rows,level.colms)
            itemsToInsert = level.magnets + level.walls + level.win
            insertInGrid(gameGrid,itemsToInsert)
            return gameGrid,level.tries
level1 = Level(1,
          3,4,
          [Magnet((1, 2)),
           PurpleMagnet((2, 0)),],
          [],[Win((1,1)),Win((1,3))],5)
      

                