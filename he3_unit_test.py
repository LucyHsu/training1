import sys
import unittest


def name_score(non_order_list):
	list_sorted = sorted(non_order_list)
	A_offset = 64
	score_list = []
	for index, value in enumerate(list_sorted):
    	    sum = 0
    	    for char_in_value in value:
        	sum += ord(char_in_value)-A_offset
	    score_list.append(sum*(index+1))
	return score_list

class test_name_score(unittest.TestCase):

	def test_correct_name_score(self):
		test_list = ['CDEF', 'ABC', 'FIJK']
		expect_name_score = [6, 36, 108]	
		self.assertEqual(name_score(test_list), expect_name_score)


if __name__ == '__main__':
    
    unittest.main()



