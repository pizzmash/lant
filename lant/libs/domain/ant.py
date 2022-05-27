from lant.libs.domain.direction import Direction
from lant.libs.domain.position import Position

class Ant:
    def __init__(self, position: Position=None, direction: Direction=None):
        self.position = position if position is not None else Position(0, 0)
        self.direction = direction if direction is not None else Direction()
    