import unittest
import draw
import filecmp
import os


class TestDrawing(unittest.TestCase):

    def test_drawing(self):
        draw.main("input.txt")
        self.assertTrue(filecmp.cmp("output.txt", "test_output.txt", shallow=False))


class TestErrorDrawing(unittest.TestCase):

    def test_error_invalid_values(self):
        with open('test_input.txt', 'w') as file:
            file.write("C 20 4\n")
            file.write("L 1 2 23 2\n")  # length = 22
        with self.assertRaises(SystemExit):
            draw.main("test_input.txt")

    def test_error_without_create(self):
        with open('test_input.txt', 'w') as file:
            file.write("R 20 4\n")  # command R first
            file.write("L 1 2 6 2\n")
        with self.assertRaises(SystemExit):
            draw.main("test_input.txt")
