import queue
import numpy as np
from GameLogic import *
from Level import Level
from PurpleMagnet import PurpleMagnet
from RedMagnet import RedMagnet

def grid_to_state(grid):
    indices = [(row, col) for row in range(grid.shape[0]) 
                         for col in range(grid.shape[1]) 
                         if isinstance(grid[row, col], (PurpleMagnet, RedMagnet))]
    return grid, indices

def get_neighbor_states(state_tuple):
    grid, index = state_tuple  
    if not index: 
        return []  
    row, col = index  
    neighbor_states = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for x, y in directions:
        new_row, new_col = row + x, col + y
        new_position = new_row, new_col
        if canMove(grid, new_row, new_col):
            new_grid = np.copy(grid)
            new_grid[row, col].Move(new_position, new_grid)
            neighbor_states.append((new_grid, (new_row, new_col)))
    
    return neighbor_states

def bfs(grid):
    start_state, indices = grid_to_state(grid)
    if not indices:
        return None  
    start_tuple = (start_state, indices)  
    visited = set()  
    q = queue.Queue()
    q.put(start_tuple)
    
    while not q.empty():
        current_state, current_indices = q.get()
        
        if len(check_win_positions(current_state)) == 0:
            return current_state
        
        current_state_tuple = tuple(map(tuple, current_state))
        
        if current_state_tuple not in visited:
            visited.add(current_state_tuple)  
            
            for index in current_indices:  
                neighbors = get_neighbor_states((current_state, index))
                
                for neighbor in neighbors:
                    neighbor_state, neighbor_index = neighbor
                    neighbor_state_tuple = tuple(map(tuple, neighbor_state))
                    
                    if neighbor_state_tuple not in visited:
                        q.put(neighbor)

def dfs(grid):
    start_state, indices = grid_to_state(grid)
    
    if not indices:
        return None  

    stack = [(start_state, index) for index in indices]  
    visited = set()  
    
    while stack:
        current_state, current_index = stack.pop()
        
        if len(check_win_positions(current_state)) == 0:
            return current_state
        
        current_state_tuple = tuple(map(tuple, current_state))
        
        if current_state_tuple not in visited:
            visited.add(current_state_tuple)  
            
            neighbors = get_neighbor_states((current_state, current_index))
            
            for neighbor in neighbors:
                neighbor_state, neighbor_index = neighbor
                neighbor_state_tuple = tuple(map(tuple, neighbor_state))
                
                if neighbor_state_tuple not in visited:
                    stack.append(neighbor)

gameGrid, tries = Level.LoadLevel(1)
bfs(gameGrid)