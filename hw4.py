import sys
import os

for a,b,file_list in os.walk("."):
	break

if len(sys.argv) == 1:
	print "Usage: hw4.py [filename]"

else:
    file_name = sys.argv[1]

    print os.path.isfile('file_name')
    print 'read file name = ', file_name, '\n'

#    if os.path.isfile("./""file_name"):
    if file_name in file_list:
	user_file = open(file_name)
        value_in_file = user_file.read()
        print value_in_file

    else: 
	print 'File not found.'



