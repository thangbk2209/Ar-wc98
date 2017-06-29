f = open('test.txt','r+a')
# print f.read()
print f.readline()
for line in f:
	print line
f.write('some thing was change\n')