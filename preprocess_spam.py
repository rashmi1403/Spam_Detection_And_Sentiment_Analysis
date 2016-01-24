from sys import argv
from os import walk


vocab_f = argv[1]		#vocab file
dir_p = argv[2]			#path of directory - HAM
output_f = argv[3]		#output file

outputfile = open(output_f, "w")

#Add vocab file into a list
vocab_list = []
filev = open(vocab_f, "r", encoding= "latin1")
line = filev.readline()
vocab_list.append("Rashmi")			#So that we can access index from 1 for the words in vocab file
while line:
	vocab_list.append(line.strip())
	line = filev.readline()

print("Finished loading vocab to list")

#files has list of all files in the dir name passed as argument
for dirname, dirnames, filenames in walk(dir_p):
	#print(filenames)
	filenames.sort()
	#print(filenames)
	
	for files in filenames:
	    #print(files)
	    fullname = dirname + "/" +files
	    #print(fullname)
	    filei = open(fullname, "r", encoding= "latin1")
	    #print("File opened")
	    #output_dictionary for each document
	    output_d = {}

	    #list of all lines in the file
	    file_lines = []
	    line = filei.readline()
	    while line:
	    	file_lines.append(line.strip())
	    	line = filei.readline()
	    
	    #for each line split into tokens 
	    for line in file_lines:
	    	tokens = []
	    	tokens = line.split(" ")
	    	for token in tokens:
	    		if(token in vocab_list):
	    			key = int(vocab_list.index(token))
	    			val = output_d.get(key)
	    			if(val != None):
	    				output_d[key] = int(val) + 1
	    			else:
	    				output_d[key] = 1
	    		else:
	    			print("Word not in vocab list = " +token)

	    

	    #After the whole document is processed, write the dictionary to the output file
	    output_res = []
	    for key in sorted(output_d):
	    	ostr = str(key) +":" + str(output_d[key])
	    	output_res.append(ostr)
	    #res = "SPAM " + " ".join(output_res)	#Change this for dev data and comment below line
	    res = " ".join(output_res)	
	    outputfile.write(res + "\n")
	    filei.close()

	print("No of files processed = " +str(len(filenames)))
filev.close()
outputfile.close()

print("Finished processing!")