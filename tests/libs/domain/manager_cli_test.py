import os
import sys
sys.path.append("./")
from lant.libs.domain.ant import Ant
from lant.libs.domain.field import Field
from lant.libs.domain.manager import Manager


class ManagerCliTest:
    def __init__(self):
        states = [Field.TurnDirection.LEFT, Field.TurnDirection.RIGHT]
        ants = [Ant()]
        self.target = Manager(Field(states), ants)
    
    def run(self) -> None:
        width = height = 31
        convert = lambda x, y: (x-(int)(width/2)-1, y-(int)(width/2)-1)
        try:
            while True:
                os.system("cls")
                for ant in self.target.ants:
                    if ant.position.to_tuple() not in self.target.field.state_map:
                        state = self.target.field.states[0]
                    else:
                        state = self.target.field.state_map[ant.position.to_tuple()]
                    print(self.target.field.TurnDirection(state))
                for y in range(height):
                    for x in range(width):
                        if convert(x, y) in [ant.position.to_tuple() for ant in self.target.ants]:
                            print("\033[41mx", end="")
                        elif convert(x, y) not in self.target.field.state_map:
                            print("\033[0m-", end="")
                        elif self.target.field.states[self.target.field.state_map[convert(x, y)]] == self.target.field.TurnDirection.LEFT:
                            print("\033[44mo", end="")
                        else:
                            print("\033[43mo", end="")
                    print("\033[0m")
                self.target.forward()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    ManagerCliTest().run()
    