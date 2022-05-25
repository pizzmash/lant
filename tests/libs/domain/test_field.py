from turtle import position
import unittest
from lant.libs.domain.field import Field
from lant.libs.domain.position import Position


class FieldTest(unittest.TestCase):
    def setUp(self) -> None:
        return
    
    def tearDown(self) -> None:
        return
    
    def test_valid_width_value(self) -> None:
        Field(1, 100)
    
    def test_invalid_width_value(self) -> None:
        with self.assertRaises(ValueError):
            Field(0, 100)
        
    def test_valid_height_value(self) -> None:
        Field(100, 1)
    
    def test_invalid_height_value(self) -> None:
        with self.assertRaises(ValueError):
            Field(100, 0)
    
    def test_init(self) -> None:
        width = 100
        height = 200
        target = Field(width, height)
        for y in range(height):
            for x in range(width):
                self.assertEqual(Field.State.UNREACHED, target.states[y][x])
    
    def test_update(self) -> None:
        width = 100
        height = 200
        target = Field(width, height)
        x = y = 0
        position = Position(width, height, x, y)
        target.update_at(position)
        self.assertEqual(Field.State.REACHED, target.states[y][x])
        target.update_at(position)
        self.assertEqual(Field.State.UNREACHED, target.states[y][x])
        