import unittest
from lant.libs.domain.direction import Direction


class DirectionTest(unittest.TestCase):
    def setUp(self) -> None:
        return
    
    def tearDown(self) -> None:
        return

    def test_init(self) -> None:
        self.assertEqual(Direction.State.NORTH, Direction(Direction.State.NORTH).state)
    
    def test_init_default(self) -> None:
        self.assertEqual(Direction.State.NORTH, Direction().state)

    def test_turn_right(self) -> None:
        direction = Direction()        
        direction.turn_right()
        self.assertEqual(Direction.State.EAST, direction.state)       
        direction.turn_right()
        self.assertEqual(Direction.State.SOUTH, direction.state)    
        direction.turn_right()
        self.assertEqual(Direction.State.WEST, direction.state)
        direction.turn_right()
        self.assertEqual(Direction.State.NORTH, direction.state)
    
    def test_turn_left(self) -> None:
        direction = Direction()        
        direction.turn_left()
        self.assertEqual(Direction.State.WEST, direction.state)       
        direction.turn_left()
        self.assertEqual(Direction.State.SOUTH, direction.state)    
        direction.turn_left()
        self.assertEqual(Direction.State.EAST, direction.state)
        direction.turn_left()
        self.assertEqual(Direction.State.NORTH, direction.state)
    