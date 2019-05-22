import unittest
import draw


class TestDrawing(unittest.TestCase):

    def test_init(self):
        self.assertEqual(pycalc.main('2+2'), 2+2)