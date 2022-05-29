from libs.domain.direction import Direction


class Position:
    def __init__(self, pos_x: int=None, pos_y: int=None):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def update_to(self, direction: Direction) -> None:
        vecotr = direction.to_vector();        
        self.pos_x = self.pos_x + vecotr[0]
        self.pos_y = self.pos_y + vecotr[1]
    
    def to_tuple(self) -> tuple:
        return (self.pos_x, self.pos_y)
    