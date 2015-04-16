#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys


TestNum = int(sys.argv[1])
print 'TestNum = ', TestNum
sum1 = 0

listtwo = [ i for i in range(1,(TestNum/2)+1) if TestNum % i ==0 ] 
print repr(TestNum) + ' is perfect number' if sum(listtwo) == TestNum else 'false'

 
