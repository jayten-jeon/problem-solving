import unittest
from problem import solution


class Test(unittest.TestCase):
    def test_input_1(self):
        board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
        r = 1
        c = 0
        result = 14
        self.assertEqual(result, solution(board, r, c))

    def test_input_1(self):
        board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
        r = 0
        c = 1
        result = 16
        self.assertEqual(result, solution(board, r, c))
