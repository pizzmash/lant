from typing import List
from libs.domain.ant import Ant
from libs.domain.field import Field


class Simulator:
    def __init__(self, field: Field, ants: List[Ant]):
        self.field = field
        self.ants = ants
        for position in {ant.position for ant in ants}:
            self.field.update_at(position)
    
    def forward(self) -> None:
        # antの位置情報一覧
        position_dict = {ant.position.to_tuple(): ant.position for ant in self.ants}
        
        # antの更新
        for ant in self.ants:
            # 現在の位置の状態を確認
            state = self.field.states[0] if ant.position.to_tuple() not in self.field.state_map else self.field.states[self.field.state_map[ant.position.to_tuple()]]
            # 進行方向の変更
            if state == self.field.TurnDirection.LEFT:
                ant.turn_left()
            else:
                ant.turn_right()
            
            # ant.positionの更新
            ant.move()
        
        # field.state_mapの更新
        for position in position_dict.values():
            self.field.update_at(position)
    