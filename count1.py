filename = raw_input("input the name of a file\n")
count = 0
myfile = open(filename, 'r')
for line in open(filename, 'r'):
	line = myfile.readline()
	count = count + 1
print count
