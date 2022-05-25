from lant.libs.domain.direction import Direction


class Position:
    def __init__(self, width: int, height: int, pos_x: int=None, pos_y: int=None):
        if width <= 0:
            raise ValueError("Invalid value. width={}".format(width))
        if height <= 0:
            raise ValueError("Invalid value. height={}".format(height))
        
        self.width = width
        self.height = height
        self.pos_x = (pos_x % width) if pos_x is not None else (int)(width / 2)
        self.pos_y = (pos_y % height) if pos_y is not None else (int)(height / 2)

    def update_to(self, direction: Direction) -> None:
        diff_tbl = {}
        diff_tbl[Direction.State.NORTH] = (0, 1)
        diff_tbl[Direction.State.EAST] = (1, 0)
        diff_tbl[Direction.State.SOUTH] = (0, -1)
        diff_tbl[Direction.State.WEST] = (-1, 0)
        
        self.pos_x = (self.pos_x + diff_tbl[direction.state][0]) % self.width
        self.pos_y = (self.pos_y + diff_tbl[direction.state][1]) % self.height
        