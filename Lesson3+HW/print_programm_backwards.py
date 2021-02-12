# программa, которая выводит
# саму себя задом наперед

import sys
filename = sys.argv[0]
f = open(filename, 'r')
for line in f:
	print(line [::-1])
f.close()
