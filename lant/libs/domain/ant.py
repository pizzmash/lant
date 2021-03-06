from libs.domain.direction import Direction
from libs.domain.position import Position

class Ant:
    def __init__(self, position: Position=None, direction: Direction=None):
        self.position = position if position is not None else Position(0, 0)
        self.direction = direction if direction is not None else Direction()
    
    def move(self) -> Position:
        self.position.update_to(self.direction)
        return self.position
    
    def turn_left(self) -> Direction:
        self.direction.turn_left()
        return self.direction
    
    def turn_right(self) -> Direction:
        self.direction.turn_right()
        return self.direction