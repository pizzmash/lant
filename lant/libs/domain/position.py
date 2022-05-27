from lant.libs.domain.direction import Direction


class Position:
    def __init__(self, pos_x: int=None, pos_y: int=None):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def update_to(self, direction: Direction) -> None:
        diff_tbl = {}
        diff_tbl[Direction.State.NORTH] = (0, 1)
        diff_tbl[Direction.State.EAST] = (1, 0)
        diff_tbl[Direction.State.SOUTH] = (0, -1)
        diff_tbl[Direction.State.WEST] = (-1, 0)
        
        self.pos_x = self.pos_x + diff_tbl[direction.state][0]
        self.pos_y = self.pos_y + diff_tbl[direction.state][1]
        