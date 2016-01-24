from sys import argv

script, inputf, outputf = argv

file1 = open(inputf, "r")
file2 = open(outputf, "w")

line = file1.readline()

#line = "9 0:9 1:1 2:4 3:4 4:6 5:4 6:2 7:2 8:4 10:4 12:2 26:1 27:1 28:1 29:2 32:1 41:1 45:1 47:1 50:1 54:2 57:1 59:1 63:2 64:1 66:1 68:2 70:1 72:1 78:1 100:1 106:1 116:1 122:1 125:1 136:1 140:1 142:1 150:1 167:1 183:1 201:1 207:1 208:1 213:1 217:1 230:1 255:1 321:5 343:1 357:1 370:1 390:2 468:1 514:1 571:1 619:1 671:1 766:1 877:1 1057:1 1179:1 1192:1 1402:2 1416:1 1477:2 1940:1 1941:1 2096:1 2243:1 2285:1 2379:1 2934:1 2938:1 3520:1 3647:1 4938:1 5138:4 5715:1 5726:1 5731:1 5812:1 8319:1 8567:1 10480:1 14239:1 20604:1 22409:4 24551:1 47304:1"

#Incrementing the feature index by 1 and  changing scores to labels
while line:
	words = line.split(" ")
	#print(words)
	#output_line = ""
	#output_line = None
	output_line = []
	""""score = int(words[0])
	if(score <= 4):
		output_line.append("NEGATIVE")
	else:
		output_line.append("POSITIVE")"""
	
	for i in range(len(words)):
		nos = words[i].split(":")
		no = int(nos[0])
		no += 1
		output_line.append(str(no) +":" + nos[1])
	file2.write(" ".join(output_line))	
	line = file1.readline()
	

file1.close()
file2.close()

print("Finished processing!")

#print(output_line)





