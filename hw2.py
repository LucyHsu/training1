
import sys

FileName = sys.argv[1]

f = open(FileName)
li = f.readlines()
f.close()


for i in range(len(li)):
    li[i] = int(li[i])


for i in range ( 0 , 3 ):
    for k in range ( len( li ) -i-1 ):
	if li[k] > li[k+1]:
	    li[k],li[k+1] = li[k+1],li[k]

print li[ ( len(li) - 3 ) : ]

 
