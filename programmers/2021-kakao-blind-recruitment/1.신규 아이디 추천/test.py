import unittest
from recommend_new_id import solution


class Tests(unittest.TestCase):
    def test_input_1(self):
        new_id = "...!@BaT#*..y.abcdefghijklm"
        result = "bat.y.abcdefghi"
        self.assertEqual(result, solution(new_id))

    def test_input_2(self):
        new_id = "z-+.^."
        result = "z--"
        self.assertEqual(result, solution(new_id))

    def test_input_3(self):
        new_id = "=.="
        result = "aaa"
        self.assertEqual(result, solution(new_id))

    def test_input_4(self):
        new_id = "123_.def"
        result = "123_.def"
        self.assertEqual(result, solution(new_id))

    def test_input_5(self):
        new_id = "abcdefghijklmn.p"
        result = "abcdefghijklmn"
        self.assertEqual(result, solution(new_id))


if __name__ == "__main__":
    unittest.main()