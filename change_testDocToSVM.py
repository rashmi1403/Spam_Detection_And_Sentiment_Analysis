from sys import argv

inputf = argv[1]
outputf = argv[2]

file1 = open(inputf, "r")	#test file without features
file2 = open(outputf, "w")	#test file with features

line = file1.readline()

while line:
	line = "0 " + line
	file2.write(line)
	line = file1.readline()

file1.close()
file2.close()

print("Finished processing!")
