import unittest
from lant.libs.domain.field import Field
from lant.libs.domain.position import Position


class FieldTest(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Field([Field.TurnDirection.LEFT,
                             Field.TurnDirection.LEFT,
                             Field.TurnDirection.RIGHT,
                             Field.TurnDirection.LEFT,
                             Field.TurnDirection.RIGHT])
        return
    
    def tearDown(self) -> None:
        return
    
    def test_update(self) -> None:
        position = Position(0, 0)
        for i in range(5):
            self.target.update_at(position)
            self.assertEqual(i, self.target.state_map[position.to_tuple()])
        self.target.update_at(position)
        self.assertEqual(0, self.target.state_map[position.to_tuple()])

        