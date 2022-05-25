from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
    @classmethod
    def right_of(cls, direction: 'Direction') -> 'Direction':
        return Direction((direction.value + 1) % len(Direction))

        
    @classmethod
    def left_of(cls, direction: 'Direction') -> 'Direction':
        return Direction((direction.value - 1) % len(Direction))
    