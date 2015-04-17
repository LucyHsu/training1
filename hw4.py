import sys

file_name_list = ['sample1.dat','sample3.dat']

if len(sys.argv) == 1:
	print "Usage: hw4.py [filename]"

else:
    file_name = sys.argv[1]

    if file_name in file_name_list:
        user_file = open(file_name)
        value_in_file = user_file.read()
        print value_in_file

    else: 
	print 'File not found.'



