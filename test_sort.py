import sys
import unittest
import sort

class test_sort_list_top3(unittest.TestCase):

    def test_case1(self):
        non_order_list = [1,4,6,3,2,8,5,7,9]
        expect_list = [7,8,9]
        self.assertEqual(sort.sort_list_top3(non_order_list), expect_list)

if __name__ == '__main__':
    unittest.main()
