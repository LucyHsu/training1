import sys
import unittest

def sort_list_top3(file_list):
    for i in range ( 0 , 3 ):
        for k in range ( len( file_list ) -1 ):
	    if file_list[k] > file_list[k+1]:
	        file_list[k],file_list[k+1] = file_list[k+1],file_list[k]
	return file_list[len(file_list)-3:]




class test_sort_list_top3(unittest.TestCase):
    
    def test_case1(self):
	non_order_list = [1,4,6,3,2,8,5,7,9]
	expect_list = [7,8,9]
	self.assertEqual(sort_list_top3(non_order_list), expect_list)





if __name__ == '__main__':
    
#    FileName = sys.argv[1]
#    f = open(FileName)
#    li = f.readlines()
#    li = [int(li[i]) for i in range(len(li))]
#    f.close()

#    sorted_li = sort_list_top3(li)
#    print sorted_li[-1],'\n',sorted_li[-2],'\n',sorted_li[-3],'\n'    
#    del sys.argv[1:]

    unittest.main()



 
