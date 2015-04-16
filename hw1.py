#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys


TestNum = int(sys.argv[1])
print 'TestNum = ', TestNum
sum = 0


 
listtwo = [sum += i for i in range(1,(TestNum/2)+1) if TestNum % i ==0 ] 
print(listtwo)

"""
for i in range(1,(TestNum/2)+1) :  
    if TestNum % i == 0:
	sum += i
"""
print repr(TestNum) + ' is perfect number' if sum == TestNum else 'false'

 
