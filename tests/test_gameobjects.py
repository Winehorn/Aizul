import unittest
from .context import aizul
from aizul import gameobjects as go


class TestTileClass(unittest.TestCase):

    def test_tile_has_color(self):
        tile = go.Tile(go.Color.BLUE)
        self.assertTrue(isinstance(tile.color, go.Color))

    def test_tile_exception_with_no_color(self):
        with self.assertRaises(TypeError):
            go.Tile("this is not a color")

class TestColorEnum(unittest.TestCase):
    def test_number_of_colors(self):
        self.assertEqual(len(go.Color),5,"Number of Colors is not 5")

if __name__ == '__main__':
    unittest.main()