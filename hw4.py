import sys
import os

if len(sys.argv) == 1:
	print "Usage: hw4.py [filename]"

else:
    file_name = sys.argv[1]
    if os.path.isfile(file_name):
	user_file = open(file_name)
	value_in_file = user_file.read()
	value_in_file_list = value_in_file.split('\n')
	cut_extra_item = value_in_file_list.pop()
	for index, value in enumerate(value_in_file_list):
            print  index+1, ':', value

    else: 
	print 'File not found.'



