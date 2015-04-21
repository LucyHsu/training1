import unittest
import perfect_number

class test_perfect_number_check(unittest.TestCase):

        def test_not_perfect_num(self):
                self.assertEqual(perfect_number.perfect_number_check(36), False)

        def test_perfect_num(self):
                self.assertEqual(perfect_number.perfect_number_check(6), True)


if __name__ == '__main__':
    unittest.main()
