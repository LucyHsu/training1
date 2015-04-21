import sys
import unittest

def sort_list_top3(file_list):
    for i in range ( 0 , 3 ):
        for k in range ( len( file_list ) -1 ):
	    if file_list[k] > file_list[k+1]:
	        file_list[k],file_list[k+1] = file_list[k+1],file_list[k]
	return file_list[len(file_list)-3:]


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



 
