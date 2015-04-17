import sys
import os



if len(sys.argv) == 1:
	print "Usage: hw4.py [filename]"



else:
    file_name = sys.argv[1]

    print os.path.isfile('file_name')
    print 'read file name = ', file_name

    if os.path.isfile("file_name"):
	user_file = open(file_name)
        value_in_file = user_file.read()
        print value_in_file

    else: 
	print 'File not found.'



