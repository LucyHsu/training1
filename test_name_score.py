import sys
import unittest
import name_score


#del sys.argv[1:]

class test_name_score(unittest.TestCase):

	def test_correct_name_score(self):
		test_list = ['CDEF', 'ABC', 'FIJK']
		expect_name_score = [6, 36, 108]	
		self.assertEqual(name_score.name_score(test_list), expect_name_score)


if __name__ == '__main__':
    
    unittest.main()



