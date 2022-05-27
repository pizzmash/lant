from typing import List
from lant.libs.domain.ant import Ant
from lant.libs.domain.field import Field


class Manager:
    def __init__(self,field: Field, ants: List[Ant]):
        self.field = field
        self.ants = ants
    
    def forward(self) -> None:
        position_set = set()
        
        # antの更新
        for ant in self.ants:
            # ant.positionの更新
            position= ant.move().to_tuple()
            
            # 移動後のpositionの状態確認
            state = 0 if position not in self.field.state_map else self.filed.states[self.field.state_map[position]]
            
            # and.directionの更新
            if self.field.states[0] == self.field.TurnDirection.LEFT:
                ant.turn_left()
            else:
                ant.turn_right()
                
            # antの位置情報一覧
            position_set |= position
            
        # field.state_mapの更新
        for position in position_set:
            self.field.update_at(position)
    