from enum import Enum


class Direction():
    class State(Enum):
        NORTH = 0
        EAST = 1
        SOUTH = 2
        WEST = 3
        
    def __init__(self, state: State=State.NORTH):
        self.state = state
    
    def turn_right(self) -> None:
        self.state = self.State((self.state.value + 1) % len(self.State))

    def turn_left(self) -> None:
        self.state = self.State((self.state.value - 1) % len(self.State))
    
    def to_vector(self) -> list:
        diff_tbl = {}
        diff_tbl[Direction.State.NORTH] = [0, 1]
        diff_tbl[Direction.State.EAST] = [1, 0]
        diff_tbl[Direction.State.SOUTH] = [0, -1]
        diff_tbl[Direction.State.WEST] = [-1, 0]
        return diff_tbl[self.state]
    