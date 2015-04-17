import sys 


file_name = sys.argv[1]
f = open(file_name)
string_in_file = f.read().strip('"\n')  # => 'CDEF","ABC","FIJK'
list_in_file = string_in_file.split('","')    # => ['CDEF', 'ABC', 'FIJK']

list_sorted = sorted(list_in_file)  # => ['ABC', 'CDEF', 'FIJK']

A_offset = 64

for index, value in enumerate(list_sorted):
    sum = 0
    for char_in_value in value:	
	sum += ord(char_in_value)-A_offset
    print value,' score= ', sum*(index+1)


