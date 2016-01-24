from sys import argv
import random

script, inputf, outputf1, outputf2 = argv
file1 = open(inputf, "r")
file2 = open(outputf1, "w")
file3 = open(outputf2, "w")


#Splitting data into 75% and 25%

line = file1.readline()
data = []
training_data = []
dev_data = []

while line:
	data.append(line)
	line = file1.readline()

#shuffle & split
random.shuffle(data)
training_data = data[:18750]
dev_data = data[18750:]

for data in training_data:
	file2.write(data)

for data in dev_data:
	file3.write(data)

file1.close()
file2.close()
file3.close()

print("Finished processing!")