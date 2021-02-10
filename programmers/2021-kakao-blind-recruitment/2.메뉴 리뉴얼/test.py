import unittest
from menu_renewal import solution


class Test(unittest.TestCase):
    def test_input_1(self):
        orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
        course = [2, 3, 4]
        expected = ["AC", "ACDE", "BCFG", "CDE"]
        result = solution(orders, course)
        self.assertListEqual(expected, result)

    def test_input_2(self):
        orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
        course = [2, 3, 5]
        expected = ["ACD", "AD", "ADE", "CD", "XYZ"]
        result = solution(orders, course)
        self.assertListEqual(expected, result)

    def test_input_3(self):
        orders = ["XYZ", "XWY", "WXA"]
        course = [2, 3, 4]
        expected = ["WX", "XY"]
        result = solution(orders, course)
        self.assertListEqual(expected, result)


if __name__ == "__main__":
    unittest.main()