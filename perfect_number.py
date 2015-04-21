#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys



def perfect_number_check(test_num):
	listtwo = [ i for i in range(1,(test_num/2)+1) if test_num % i ==0 ] 
	# print repr(test_num) + ' is perfect number' if sum(listtwo) == test_num else 'false'
	return True if sum(listtwo) == test_num else False

if __name__ == '__main__':
    # TestNum = int(sys.argv[1])
    # print 'TestNum = ', TestNum
    sum1 = 0
    # perfect_number_check(TestNum)
    # del sys.argv[1:]
    unittest.main()

 
