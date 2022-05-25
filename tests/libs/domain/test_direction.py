import unittest
from lant.libs.domain.direction import Direction


class DirectionTest(unittest.TestCase):
    def setUp(self) -> None:
        return
    
    def tearDown(self) -> None:
        return

    def test_value_of(self) -> None:
        self.assertEqual(Direction.NORTH, Direction(0))
        self.assertEqual(Direction.EAST, Direction(1))
        self.assertEqual(Direction.SOUTH, Direction(2))
        self.assertEqual(Direction.WEST, Direction(3))

    def test_right_of(self) -> None:
        self.assertEqual(Direction.EAST, Direction.right_of(Direction.NORTH))
        self.assertEqual(Direction.SOUTH, Direction.right_of(Direction.EAST))
        self.assertEqual(Direction.WEST, Direction.right_of(Direction.SOUTH))
        self.assertEqual(Direction.NORTH, Direction.right_of(Direction.WEST))
    
    def test_left_of(self) -> None:
        self.assertEqual(Direction.WEST, Direction.left_of(Direction.NORTH))
        self.assertEqual(Direction.NORTH, Direction.left_of(Direction.EAST))
        self.assertEqual(Direction.EAST, Direction.left_of(Direction.SOUTH))
        self.assertEqual(Direction.SOUTH, Direction.left_of(Direction.WEST))
    