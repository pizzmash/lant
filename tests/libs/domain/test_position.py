import unittest
from lant.libs.domain.position import Position


class PositionTest(unittest.TestCase):
    def setUp(self) -> None:
        return
    
    def tearDown(self) -> None:
        return
    
    def test_valid_width_value(self) -> None:
        Position(1, 100, 50, 50)
    
    def test_invalid_width_value(self) -> None:
        with self.assertRaises(ValueError):
            Position(0, 100, 50, 50)
        
    def test_valid_height_value(self) -> None:
        Position(100, 1, 50, 50)
    
    def test_invalid_height_value(self) -> None:
        with self.assertRaises(ValueError):
            Position(100, 0, 50, 50)
    
    def test_init_even_pos_value(self) -> None:
        position = Position(100, 200)
        self.assertEqual(50, position.pos_x)
        self.assertEqual(100, position.pos_y)
    
    def test_init_odd_pos_value(self) -> None:
        position = Position(101, 201)
        self.assertEqual(50, position.pos_x)
        self.assertEqual(100, position.pos_y)
    