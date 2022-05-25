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
    