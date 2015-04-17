import sys 


FileName = sys.argv[1]
f = open(FileName)
str = f.read()
str = str.strip('"\n')   # => 'CDEF","ABC","FIJK'
li = str.split('","')    # => ['CDEF', 'ABC', 'FIJK']

for i in range(len(li)-1):
    if li[i]>li[i+1]:
	li[i],li[i+1] = li[i+1],li[i]  # => ['ABC', 'CDEF', 'FIJK']

list = []

for i in range(len(li)):
    temp_str = li[i]
    temp_list = []
    for k in range(0,len(temp_str)):
	temp_list.append(temp_str[k])
    list.append(temp_list)             # => [['A', 'B', 'C'], ['C', 'D', 'E', 'F'], ['F', 'I', 'J', 'K']]


for i in range(len(li)):
    temp_list= list.pop()
    sum = 0
    for k in range(len(temp_list)):
	sum += ord(temp_list[k])-64
    print li[(len(li)-i-1)],' score = ', sum*(len(li)-i) 

