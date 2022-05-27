import unittest
from lant.libs.domain.direction import Direction
from lant.libs.domain.position import Position


class PositionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Position(0, 0)
    
    def tearDown(self) -> None:
        return
    
    def test_update_to_north(self) -> None:
        self.target.update_to(Direction(Direction.State.NORTH))
        self.assertEqual(self.target.pos_x, 0)
        self.assertEqual(self.target.pos_y, 1)
        
    def test_update_to_east(self) -> None:
        self.target.update_to(Direction(Direction.State.EAST))
        self.assertEqual(self.target.pos_x, 1)
        self.assertEqual(self.target.pos_y, 0)
        
    def test_update_to_south(self) -> None:
        self.target.update_to(Direction(Direction.State.SOUTH))
        self.assertEqual(self.target.pos_x, 0)
        self.assertEqual(self.target.pos_y, -1)
        
    def test_update_to_west(self) -> None:
        self.target.update_to(Direction(Direction.State.WEST))
        self.assertEqual(self.target.pos_x, -1)
        self.assertEqual(self.target.pos_y, 0)
    
    